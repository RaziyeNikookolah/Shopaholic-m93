from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from ..models import Account  # Adjust this import as needed


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = Account.objects.create(phone_number='1234567890')
        self.client.force_login(self.user)

    def test_login_view(self):
        url = reverse('login')  # Adjust this based on your URL configuration
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_view(self):
        url = reverse('logout')  # Adjust this based on your URL configuration
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_logout_view(self):
        # Adjust this based on your URL configuration
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_view(self):
        url = reverse('profile')  # Adjust this based on your URL configuration
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertIn('PROVINCES', response.context)
