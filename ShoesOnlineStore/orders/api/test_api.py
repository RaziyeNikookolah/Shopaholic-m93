from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from ..models import Order
from orders.serializer import OrderSerializer
from ..views import ListOrder

class ListOrderViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ListOrder.as_view({'get': 'list'})
        self.url = reverse('order-list')  # Assuming you're using DefaultRouter

    def test_list_orders(self):
        order = Order.objects.create(account=..., ...)  # Create an order as needed
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        expected_data = OrderSerializer([order], many=True).data
        self.assertEqual(response.data, expected_data)

    # Add more test cases as needed

