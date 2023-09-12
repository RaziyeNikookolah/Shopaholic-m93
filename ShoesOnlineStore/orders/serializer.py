from .models import Order
from rest_framework import serializers
from .models import OrderItem
from shoes.models import Product
from shoes.serializer import ProductsSerializer, ProductSimpleSerializer
from django.conf import settings

# Fetch configuration constants from settings
MAX_DIGITS = settings.MAX_DIGITS
DECIMAL_PLACES = settings.DECIMAL_PLACES

# Serializer for order items within an order


class OrderItemsSerializer(serializers.Serializer):
    product = ProductSimpleSerializer()  # Serialize the related product details
    total_price = serializers.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)  # Total price for this order item
    quantity = serializers.IntegerField()  # Quantity of the product in the order

    # Additional method to calculate total price (currently commented out)
    # def get_total_price(self, orderItem):
    #     return orderItem.quantity * orderItem.product.last_price

# Serializer for individual cart items


class CartItemSerializer(serializers.Serializer):
    total_price = serializers.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)  # Total price for this cart item
    product_id = serializers.CharField(
        max_length=4)  # Product ID for this cart item
    quantity = serializers.IntegerField()  # Quantity of the product in the cart
    price = serializers.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)  # Price of the product

# Serializer for removing items from the cart


class RemoveCartItemsSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()  # Product ID of the item to be removed

# Serializer for the Order model


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order  # Define the model to be serialized
        fields = '__all__'  # Include all fields from the model in the serialization
