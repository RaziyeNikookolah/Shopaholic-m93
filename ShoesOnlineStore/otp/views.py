from datetime import datetime, timezone
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
        # throttle_classes = [OncePerMinuteThorttle]
        serializer = RequestOtpSerializer(data=request.data)
        if serializer.is_valid():

            # now user send me his phone number and other data in request
            # in serializer we just work with request.data
            otp_request = OtpRequest()
            otp_request.phone_number = serializer.validated_data['phone_number']
            otp_request.generate_code()
            otp_request.save()

            try:
                api = KavenegarAPI(settings.SMS_API_KEY)
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
                return Response({'error': 'Failed to send OTP because of kavenegar api authorization...'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except HTTPException as e:
                print(e)
                return Response({'error': 'Failed to send OTP'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtp(APIView):
    def post(self, request):
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid():
            query = OtpRequest.objects.filter(
                phone_number=serializer.validated_data['phone_number'],
                valid_until__gte=datetime.now(timezone.utc)
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
                return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
