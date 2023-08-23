from orders.serializer import OrderSerializer
from ..models import Order
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import serializers


class ListOrder(ViewSet):
    account = serializers.StringRelatedField(read_only=True)
    queryset = Order.objects.all()
    http_method_names = ['get']

    def list(self, request):
        serializer = OrderSerializer(self.queryset, many=True)
        return Response(serializer.data)


router = DefaultRouter()
router.register(r'orders', ListOrder, basename='order')
