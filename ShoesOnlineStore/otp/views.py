from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from http.client import HTTPException
from .serializers import RequestOtpSerializer, VerifyOtpSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from kavenegar import KavenegarAPI, APIException
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OtpRequest
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
            print("*****  "+otp_request.code+"  *****")
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
                return Response({"message": "OTP send successfully"})
            except APIException as e:
                print(e)
                return Response({'message': 'Send OTP of kavenegar without api authorization...'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except HTTPException as e:
                print(e)
                return Response({'error': 'Failed to send OTP'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtp(APIView):
    def post(self, request):
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            code = serializer.validated_data['code']
            otp_requests = OtpRequest.objects.filter(phone_number=phone_number)
            if otp_requests.exists():

                otp_request = otp_requests.first()

                if otp_request.is_expired():

                    messages.error(request, _(
                        'Too late receive a code.'), 'danger')
                    otp_request.delete()
                    return Response(serializer.errors, status=status.HTTP_200_OK)

                if code == otp_request.code:

                    messages.success(request, _(
                        'Your code verified..'), 'success')
                    User = get_user_model()
                    otp_request.delete()
                    if not User.objects.filter(phone_number=phone_number).exists():

                        user = User.objects.create(
                            phone_number=phone_number)
                        # create jwt token
                        # goes to profile page
                        # token, created = Token.objects.get_or_create(
                        #     user=user)
                        return Response({'message': 'Code Verified'}, status=status.HTTP_202_ACCEPTED)
                    # login mishe

                    return Response({'message': 'Code Verified'}, status=status.HTTP_202_ACCEPTED)
                else:

                    messages.error(request, _(
                        'Invalid code..'), 'danger')
                    otp_request.delete()
                    return Response({'error': 'Invalid code.'}, status=status.HTTP_403_FORBIDDEN)
            else:

                return Response({'error': 'Invalid data provided.'}, status=status.HTTP_403_FORBIDDEN)
        else:

            return Response({'error': 'Invalid data provided.'}, status=status.HTTP_400_BAD_REQUEST)
