from rest_framework import serializers
from orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        exclude = ('id',)


class OrdersSerializer(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField()
    account = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ['account', 'sending_type', 'delivery_status', 'is_paid', 'payment_date', 'tracking_code', 'shipping_cost', 'sent_date', 'delivery_date', 'tax', 'self_receive',
                  'receiver_name', 'receiver_lastname', 'email', 'province', 'receiver_phone_number', 'city', 'address', 'postal_code', 'note', 'orderItems']

    def get_orderItems(self, obj):
        result = obj.items.all()
        return OrderItemSerializer(instance=result, many=True).data
