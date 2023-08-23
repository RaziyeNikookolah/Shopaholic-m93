from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from ..models import Order, OrderItem
from accounts.models import Account
from shoes.models import Product
from decimal import Decimal
import json


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Account.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.product = Product.objects.create(name='Test Product')
        self.order = Order.objects.create(account=self.user)

    def test_add_to_cart(self):
        url = reverse('add_to_cart')
        data = {
            'product_id': self.product.id,
            'quantity': 2,
            'price': Decimal('50.00'),
            'total_price': Decimal('100.00')
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Add more test cases for other views similarly

    def test_export(self):
        url = reverse('export')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add assertions to check the content of the CSV file

    def test_create_order(self):
        url = reverse('create_order')
        data = {
            'fname': 'John',
            'lname': 'Doe',
            'address': '123 Main St',
            'city': 'City',
            'province': 'Province',
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'postal_zip': '12345',
            'order_note': 'Test order'
        }
        self.client.force_login(self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Add assertions to check the response data and created order

        order = Order.objects.filter(account=self.user, is_paid=False).first()
        self.assertIsNotNone(order)

        order_items = OrderItem.objects.filter(order=order)
        self.assertGreater(len(order_items), 0)
