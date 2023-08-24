from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User  # Assuming you have a User model


class UrlsTestCase(TestCase):
    def setUp(self):
        # Create a user for the authentication test
        self.user = User.objects.create_user(
            username='testuser', password='testpass')

    def test_admin_url(self):
        url = reverse('admin:index')
        self.assertEqual(resolve(url).func.__name__, 'index')

    def test_shoes_url(self):
        url = reverse('shoes:some_view_name')  # Replace with actual view name
        # Replace with actual view function name
        self.assertEqual(resolve(url).func.__name__, 'some_view_function')

    def test_accounts_url(self):
        # Replace with actual view name
        url = reverse('accounts:some_view_name')
        # Replace with actual view function name
        self.assertEqual(resolve(url).func.__name__, 'some_view_function')

    # Add similar tests for other URLs

    def test_authenticated_api_auth_url(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('rest_framework:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_anonymous_api_auth_url(self):
        url = reverse('rest_framework:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Add similar tests for other URLs
