from rest_framework import serializers
from accounts.models import OtpRequest


class RequestOtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=12)


class ResponseOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpRequest
        fields = ['request_id']


class VerifyOtpSerializer(serializers.Serializer):
    request_id = serializers.CharField(max_length=64)
    phone_number = serializers.CharField(max_length=12)
    code = serializers.CharField(max_length=4)


class VerifyOtpResponseSerializer(serializers.Serializer):
    token = serializers.BooleanField()
    new_user = serializers.BooleanField()
