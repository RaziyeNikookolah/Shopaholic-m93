from rest_framework import serializers


class RequestOtpSerializer(serializers.Serializer):
    phon_number = serializers.CharField(max_length=12, null=False)


class ResponseOtpSerializer(serializers.Serializer):
    ...


class VerifyOtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=12, null=False)
    password = serializers.CharField(null=True)


class VerifyOtpResponseSerializer(serializers.Serializer):
    token = serializers.BooleanField()
    new_user = serializers.BooleanField()
