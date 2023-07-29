from datetime import datetime, timezone
from rest_framework import serializers
from accounts.models import OtpRequest


class RequestOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpRequest
        fields = ['phone_number']


class VerifyOtpSerializer(serializers.Serializer):
    # request_id = serializers.CharField(max_length=64)
    phone_number = serializers.CharField(max_length=12)
    code = serializers.CharField(max_length=4)


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=250)
