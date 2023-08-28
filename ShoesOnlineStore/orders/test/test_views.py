
from ..utils import session_cart, add_product_to_session, clear_session
from ..models import Order  # Import your models
from decimal import Decimal
from rest_framework.test import APIClient
from django.test import TestCase
from model_bakery import baker
from accounts.models import Account
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from shoes.models import SHOES_SIZE_NAME, Price, Product, Size

User = get_user_model()


class CreateOrderViewTest(APITestCase):
    def setUp(self):
        self.user = baker.make(User, phone_number="09876543")
        self.product = baker.make(
            Product)
        self.price = baker.make(Price, product=self.product)
        self.size = baker.make(Size, name=SHOES_SIZE_NAME.ADULT)
        self.product.size.add(self.size)

        self.client.force_authenticate(user=self.user)

    def test_create_order(self):
        url = reverse('create_order')
        data = {
            'fname': 'John',
            'lname': 'Doe',
            'address': '123 Main St',
            'city': 'New York',
            'province': 'NY',
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'postal_zip': '12345',
            'order_note': 'Test order',
        }

        # Manually set session data
        session = self.client.session
        session['products'] = {
            str(self.product.id): {'price': '50', 'quantity': 2, 'total_price': '100'}
        }
        session.save()

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Order added successfully')
