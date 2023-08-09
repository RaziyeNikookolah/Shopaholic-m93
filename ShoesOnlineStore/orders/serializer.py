from rest_framework import serializers
from .models import OrderItems
from shoes.serializer import ProductsSerializer
from django.conf import settings

MAX_DIGITS = settings.MAX_DIGITS
DECIMAL_PLACES = settings.DECIMAL_PLACES


class OrderItemsSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = OrderItems
        fields = "__all__"


class AddCartItemsSerializer(serializers.Serializer):
    product_id = serializers.CharField(max_length=4)
    image = serializers.CharField(max_length=240)
    quantity = serializers.CharField(max_length=4)
    color = serializers.CharField(max_length=40)
    size = serializers.IntegerField()
    price = serializers.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)


class RemoveCartItemsSerializer(serializers.Serializer):
    product_id = serializers.CharField(max_length=4)


class CartItemSerializer(serializers.Serializer):

    image = serializers.CharField(max_length=240)
    quantity = serializers.CharField(max_length=4)
    color = serializers.CharField(max_length=40)
    size = serializers.IntegerField()
    price = serializers.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    total_price = serializers.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
