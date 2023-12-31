from rest_framework import status
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from http.client import HTTPException
from kavenegar import KavenegarAPI, APIException
from django.conf import settings
from rest_framework.response import Response


def send_otp_request(otp_request):
    try:
        api = KavenegarAPI(settings.SMS_API_KEY)
        params = {
            'receptor': otp_request.phone_number,
            'template': 'کد تایید شما',
            'token': otp_request.code,
            'type': 'sms',  # sms vs call
        }
        response = api.verify_lookup(params)
        return status.HTTP_200_OK, "OTP send successfully"
    except APIException as e:
        return status.HTTP_500_INTERNAL_SERVER_ERROR, 'Send OTP of kavenegar without api authorization...'
    except HTTPException as e:
        return status.HTTP_500_INTERNAL_SERVER_ERROR, 'Failed to send OTP'


def verify_otp_request(code, otp_request):

    if otp_request.is_expired():
        otp_request.delete()
        return status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, "Too late receive a code"

    if code == otp_request.code:
        otp_request.delete()
        return status.HTTP_200_OK, 'verified'

    else:
        otp_request.delete()
        return status.HTTP_403_FORBIDDEN, 'Invalid code'
