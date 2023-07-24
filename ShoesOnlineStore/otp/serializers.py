from datetime import datetime, timezone
from rest_framework import serializers
from accounts.models import OtpRequest


class RequestOtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=12)


class ResponseOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpRequest
        fields = "__all__"


class VerifyOtpSerializer(serializers.Serializer):
    # request_id = serializers.CharField(max_length=64)
    phone_number = serializers.CharField(max_length=12)
    code = serializers.CharField(max_length=4)

    def validate(self, data):
        # request_id = data.get('request_id')
        phone_number = data.get('phone_number')
        code = data.get('code')

        try:
            otp_request = OtpRequest.objects.get(
                # request_id=request_id,
                phone_number=phone_number,
            )
        except OtpRequest.DoesNotExist:
            raise serializers.ValidationError('Invalid OTP request.')

        if otp_request.valid_until < datetime.now(timezone.utc):
            raise serializers.ValidationError(
                'Invalid OTP or OTP has expired.')

        if otp_request.code != code:
            raise serializers.ValidationError('Invalid OTP.')

        return data


class VerifyOtpResponseSerializer(serializers.Serializer):
    token = serializers.BooleanField()
    new_user = serializers.BooleanField()
