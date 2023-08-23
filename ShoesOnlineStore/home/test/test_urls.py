from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class URLTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_home_url(self):
        response = self.client.get(reverse('home:index'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_about_url(self):
        response = self.client.get(reverse('home:about'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cart_url(self):
        response = self.client.get(reverse('home:cart'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contact_url(self):
        response = self.client.get(reverse('home:contact'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shop_url(self):
        response = self.client.get(reverse('home:shop'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shop_single_url(self):
        product_id = 1  # Replace with an actual product ID
        response = self.client.get(
            reverse('home:shop_single', args=[product_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_thank_you_url(self):
        response = self.client.get(reverse('home:thank_you'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_checkout_url(self):
        response = self.client.get(reverse('home:checkout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shoe_detail_url(self):
        product_id = 1  # Replace with an actual product ID
        response = self.client.get(
            reverse('home:shoe_detail', args=[product_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
