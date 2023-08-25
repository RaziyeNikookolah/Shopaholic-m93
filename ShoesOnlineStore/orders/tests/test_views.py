from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Order


class ViewsTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_add_to_cart_view(self):
        # Test your AddToCartView here
        # Example: Send a POST request to the view and assert the response status code
        response = self.client.post(
            '/your-url/add-to-cart/', {'product_id': 'example_id', 'quantity': 2})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_remove_cart_item_view(self):
        # Test your RemoveCartItemView here
        # Example: Send a POST request to the view and assert the response status code
        response = self.client.post(
            '/your-url/remove-cart-item/', {'product_id': 'example_id'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # You can add similar tests for other views

    def test_create_order_view(self):
        # Test your CreateOrder view here
        # Example: Send a POST request to the view and assert the response status code
        response = self.client.post(
            '/your-url/create-order/', {'fname': 'John', 'lname': 'Doe', 'address': 'Example Address'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # You can add more test methods for your other views

    # For tests related to sessions, you might want to use Django's Client session
    # Example:
    def test_session_cart(self):
        session = self.client.session
        session['your_key'] = 'your_value'
        session.save()
        response = self.client.get('/your-url/cart-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('your_key'), 'your_value')
