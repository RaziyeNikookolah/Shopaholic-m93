from django.test import TestCase
from django.urls import reverse


class URLTests(TestCase):
    def test_order_create_url(self):
        url = reverse('order_create')
        self.assertEqual(url, '/create/')

    def test_cart_list_url(self):
        url = reverse('cart_list')
        self.assertEqual(url, '/cart_list/')

    def test_add_to_cart_url(self):
        url = reverse('add_to_cart')
        self.assertEqual(url, '/add_to_cart/')

    def test_remove_from_cart_url(self):
        url = reverse('remove_from_cart')
        self.assertEqual(url, '/remove_from_cart/')

    def test_update_cart_url(self):
        url = reverse('update_cart')
        self.assertEqual(url, '/update_cart/')

    def test_checkout_url(self):
        url = reverse('checkout')
        self.assertEqual(url, '/checkout/')

    def test_create_order_url(self):
        url = reverse('create_order')
        self.assertEqual(url, '/create_order/')

    def test_export_url(self):
        url = reverse('export')
        self.assertEqual(url, '/export/')

    def test_request_url(self):
        url = reverse('request')
        self.assertEqual(url, '/request/')

    def test_verify_url(self):
        url = reverse('verify')
        self.assertEqual(url, '/verify/')
