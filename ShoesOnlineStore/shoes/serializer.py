from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User


class ProductsSerializer(serializers.ModelSerializer):
    # brand = serializers.StringRelatedField(read_only=True)
    # color = serializers.StringRelatedField(many=True, read_only=True)
    # category = serializers.StringRelatedField(read_only=True)
    # size = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
