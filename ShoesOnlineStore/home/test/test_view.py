from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class ViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shop_view(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cart_view(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_checkout_view(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shop_single_view(self):
        product_id = 1  # Replace with an actual product ID
        response = self.client.get(reverse('shop_single', args=[product_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_thankyou_view(self):
        response = self.client.get(reverse('thankyou'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shoe_detail_view(self):
        product_id = 1  # Replace with an actual product ID
        response = self.client.get(reverse('shoe_detail', args=[product_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
