import re
from rest_framework import serializers
from .models import OtpRequest


class RequestOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpRequest
        fields = ['phone_number']

    def validate_phone_number(self, value):
        regex = re.compile(r'^(?:\+98|0|98)?9\d{9}$')
        if not regex.match(value):
            raise serializers.ValidationError("Invalid phone number")
        return value


class VerifyOtpSerializer(serializers.Serializer):
    # request_id = serializers.CharField(max_length=64)
    phone_number = serializers.CharField(max_length=12)
    code = serializers.CharField(max_length=4)
