from django.utils.translation import gettext_lazy as _
from .serializers import RequestOtpSerializer, VerifyOtpSerializer
from .utils import send_otp_request, verify_otp_request
from accounts.utils import generate_access_token, generate_refresh_token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OtpRequest
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import AllowAny
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt


# to manage user prompt request and response time period
class OncePerMinuteThorttle(UserRateThrottle):
    rate = '1/minute'


class RequestOTP(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = []

    @csrf_exempt
    def post(self, request):
        # throttle_classes = [OncePerMinuteThorttle]
        serializer = RequestOtpSerializer(data=request.data)
        if serializer.is_valid():
            otp_request = OtpRequest()
            otp_request.phone_number = serializer.validated_data['phone_number']
            otp_request.generate_code()
            print("*****  "+otp_request.code+"  *****")
            otp_request.save()

            return send_otp_request(otp_request)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtp(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = []

    def post(self, request):
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            code = serializer.validated_data['code']
            otp_requests = OtpRequest.objects.filter(phone_number=phone_number)
            if otp_requests.exists():
                otp_request = otp_requests.first()
                verification_status, message = verify_otp_request(
                    code, otp_request)
                if verification_status == status.HTTP_200_OK:
                    User = get_user_model()
                    user: User
                    user, _ = User.objects.get_or_create(
                        phone_number=phone_number)
                    login(request, user)
                    print(user)
                    # add_session_items_to_orderItem(user)

                    # create jwt token
                    access_token = generate_access_token(user)
                    refresh_token = generate_refresh_token(user)
                    if 'next' in request.POST:
                        return Response({"access_token": access_token, "refresh_token": refresh_token,
                                         "redirect_url": request.POST.get('next')}, status=verification_status)
                    else:
                        return Response({"access_token": access_token, "refresh_token": refresh_token}, status=verification_status)

                    # goes to profile page
                else:
                    if 'next' in request.POST:
                        return Response({'message': message, "redirect_url": request.POST.get('next')}, status=verification_status)
                    else:
                        return Response({'message': message}, status=verification_status)

            else:
                return Response({'error': 'Invalid data provided.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid data provided.'}, status=status.HTTP_403_FORBIDDEN)
