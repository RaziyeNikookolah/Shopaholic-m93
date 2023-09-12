from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from django.contrib.sessions.backends.db import SessionStore
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..utils import session_cart, add_product_to_session, clear_session

from model_bakery import baker

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
            str(self.product.id): {'price': 50, 'quantity': 2, 'total_price': 100}
        }
        session.save()

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Order added successfully')
        self.client.session.clear()


class UpdateCartItemViewTest(APITestCase):
    def setUp(self):
        # Adjust this to match your URL configuration
        self.url = reverse("update_cart")
        self.product = baker.make(
            Product, id=1)
        self.price = baker.make(Price, product=self.product)
        self.size = baker.make(Size, name=SHOES_SIZE_NAME.ADULT)
        self.product.size.add(self.size)

    def test_update_cart_items(self):
        # Create some initial test data
        product_data = {
            "id": 1,
            "price": 50,
            "quantity": 2,
            "sub_total": 100
        }
        cart_items = {"1": product_data}

        data = {"cart_items": cart_items}

        response = self.client.post(self.url, data, format="json")

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert session data has been updated
        updated_cart = session_cart()
        self.assertIn("cart_items", updated_cart)
        self.assertEqual(len(updated_cart["cart_items"]), 1)
        self.client.session.clear()

    def test_update_cart_items_bad_data(self):
        # Test with bad data (missing cart_items)
        response = self.client.post(self.url, {}, format="json")

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.client.session.clear()


class CartListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('orders.views.session_cart')  # Mock the session_cart function
    def test_get_cart_data(self, mock_session_cart):
        mock_session_cart.return_value = {
            "cart_items": {
                "1": {
                    "id": 1,
                    "name": "Product 1",
                    "price": "50.00",
                    "quantity": 2,
                    "sub_total": "100.00",
                },
                "2": {
                    "id": 2,
                    "name": "Product 2",
                    "price": "75.00",
                    "quantity": 1,
                    "sub_total": "75.00",
                },
            },
            "grand_total": "175.00",
        }

        # Replace with your actual URL
        url = reverse('cart_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            "cart_items": {
                "1": {
                    "id": 1,
                    "name": "Product 1",
                    "price": "50.00",
                    "quantity": 2,
                    "sub_total": "100.00",
                },
                "2": {
                    "id": 2,
                    "name": "Product 2",
                    "price": "75.00",
                    "quantity": 1,
                    "sub_total": "75.00",
                },
            },
            "grand_total": "175.00",
        }
        self.assertEqual(response.data, expected_data)


class AddToCartViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    # Mock the add_product_to_session function
    @patch('orders.views.add_product_to_session')
    def test_add_to_cart(self, mock_add_product_to_session):
        def check_arguments(product_id, price, quantity, total_price):
            self.assertEqual(int(product_id), 1)
            self.assertEqual(price, 50)
            self.assertEqual(quantity, 2)
            self.assertEqual(total_price, 100)

        mock_add_product_to_session.side_effect = check_arguments

        data = {
            "product_id": 1,
            "quantity": 2,
            "price": '50',  # Keep as string
            "total_price": '100',  # Keep as string
        }
        url = reverse("add_to_cart")
        response = self.client.post(
            url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'message': 'item_added'})

    def test_invalid_data(self):
        data = {
            "product_id": 1,
            "quantity": -1,  # Invalid quantity
            "price": '50',  # Keep as string
            "total_price": '100',  # Keep as string
        }
        url = reverse("add_to_cart")
        response = self.client.post(
            url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
