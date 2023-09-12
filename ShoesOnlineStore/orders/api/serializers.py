from rest_framework import serializers
from orders.models import Order, OrderItem

# Serializer for OrderItem model


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        exclude = ('id',)  # Exclude 'id' field from serialization

# Serializer for Order model


class OrdersSerializer(serializers.ModelSerializer):
    # Custom field to serialize order items
    orderItems = serializers.SerializerMethodField()
    account = serializers.StringRelatedField(
        read_only=True)  # Serialize related account details

    class Meta:
        model = Order  # Define the model to be serialized
        fields = ['account', 'sending_type', 'delivery_status', 'is_paid', 'payment_date', 'tracking_code', 'shipping_cost', 'sent_date', 'delivery_date', 'tax', 'self_receive',
                  'receiver_name', 'receiver_lastname', 'email', 'province', 'receiver_phone_number', 'city', 'address', 'postal_code', 'note', 'orderItems']  # Specify fields to be serialized

    def get_orderItems(self, obj):
        result = obj.items.all()  # Retrieve all related OrderItems for this Order
        # Serialize the OrderItems using the OrderItemSerializer
        return OrderItemSerializer(instance=result, many=True).data
