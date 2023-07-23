from datetime import datetime
from rest_framework.authtoken.models import Token
from http.client import HTTPException
from .serializers import RequestOtpSerializer, ResponseOtpSerializer, VerifyOtpSerializer, VerifyOtpResponseSerializer
from kavenegar import KavenegarAPI, APIException
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import OtpRequest
from rest_framework.throttling import UserRateThrottle

# to manage user prompt request and response time period


class OncePerMinuteThorttle(UserRateThrottle):
    rate = '1/minute'


class RequestOTP(APIView):
    def post(self, request):
        throttle_classes = [OncePerMinuteThorttle]
        serializer = RequestOtpSerializer(data=request.data)
        if serializer.is_valid():

            # now user send me his phone number and other data in request
            # in serializer we just work with request.data
            otp_request = OtpRequest()
            otp_request.phone_number = serializer.validated_data['phone_number']
            otp_request.generate_code()
            otp_request.save()

            api = KavenegarAPI(settings.SMS_API_KEY)
            response = api.verify_lookup({
                'receptor': otp_request.phone_number,
                'token': otp_request.code,
                'template': settings.OTP_TEMPLATE
            })
            try:
                api = KavenegarAPI(settings.SMS_API_KEY, timeout=20)
                params = {
                    'receptor': otp_request.phone_number,
                    'template': 'کد تایید شما',
                    'token': otp_request.code,
                    'type': 'sms',  # sms vs call
                }
                response = api.verify_lookup(params)
                print(response)
                return Response(ResponseOtpSerializer(otp_request).data)
            except APIException as e:
                print(e)
            except HTTPException as e:
                print(e)

        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtp(APIView):
    def post(self, request):
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid():
            query = OtpRequest.objects.filter(
                request_id=serializer.validated_data['request_id'],
                phone_number=serializer.validated_data['phone_number'],
                valid_until__gte=datetime.now()
            )
            if query.exists():
                User = get_user_model()
                user = User.objects.filter(
                    phone_number=serializer.validated_data['phone_number'])
                if user.exists():
                    token, created = Token.objects.get_or_create(
                        user=user.first())
                    return Response(VerifyOtpResponseSerializer(data={'token': token, 'new_uesr': False}).data)
                else:
                    user = User.objects.create(
                        phone_number=serializer.validated_data['phone_number'])
                    token, created = Token.objects.get_or_create(
                        user=user.first())
                    return Response(VerifyOtpResponseSerializer(data={'token': token, 'new_uesr': True}).data)

            else:
                return Response(None, status=status.HTTP_403_FORBIDDEN)

        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
