from rest_framework import serializers

from accounts.models import Account, Address, Profile


class ProfileSerializer(serializers.ModelSerializer):
    account = serializers.CharField(source="account.phone_number")

    class Meta:
        model = Profile
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    addresses = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ['phone_number', 'profile', 'addresses']

    def get_addresses(self, obj):
        result = obj.addresses.all()  # Retrieve all related Addresses for this Profile
        return AddressSerializer(instance=result, many=True).data

    def get_profile(self, obj):
        result = Profile.objects.filter(account=obj)
        if result.exists():
            return ProfileSerializer(instance=result.first(), many=False).data
        else:
            return None
