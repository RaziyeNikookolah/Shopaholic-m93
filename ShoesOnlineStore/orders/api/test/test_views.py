from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import Account

from shoes.models import Price, Product
from ...models import Order, OrderItem
from ..serializers import OrdersSerializer
from model_bakery import baker


class OrdersViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Account.objects.create(phone_number='1234567890')
        self.client.force_authenticate(user=self.user)

        self.product1 = baker.make(Product)
        self.product2 = baker.make(Product)
        self.price1 = baker.make(Price, product=self.product1, price=100)
        self.price2 = baker.make(Price, product=self.product2, price=100)
        self.account = baker.make(Account)
        self.order = baker.make(Order, account=self.account)
        self.orderItem1 = baker.make(
            OrderItem, order=self.order, product=self.product1)
        self.orderItem2 = baker.make(
            OrderItem, order=self.order, product=self.product2)

    def test_list_orders(self):
        # Replace with the actual URL
        response = self.client.get('/api/v1/orders/orders/')
        orders = Order.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
