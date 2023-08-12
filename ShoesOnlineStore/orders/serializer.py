from rest_framework import serializers
from .models import OrderItems
from shoes.models import Product
from shoes.serializer import ProductsSerializer, ProductSimpleSerializer
from django.conf import settings

MAX_DIGITS = settings.MAX_DIGITS
DECIMAL_PLACES = settings.DECIMAL_PLACES


class OrderItemsSerializer(serializers.Serializer):
    product = ProductSimpleSerializer()
    total_price = serializers.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)  # SerializerMethodField()
    quantity = serializers.IntegerField()

    # def get_total_price(self, orderItem):
    #     return orderItem.quantity*orderItem.product.last_price


class CartItemSerializer(serializers.Serializer):
    total_price = serializers.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    product_id = serializers.CharField(max_length=4)
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)


class RemoveCartItemsSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
