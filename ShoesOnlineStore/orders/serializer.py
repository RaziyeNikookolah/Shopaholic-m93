from rest_framework import serializers
from .models import OrderItems
from shoes.serializer import ProductsSerializer


class OrderItemsSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = OrderItems
        fields = "__all__"


class CartItemsSerializer(serializers.Serializer):
    product_id = serializers.CharField(max_length=4)
    quantity = serializers.CharField(max_length=4)
