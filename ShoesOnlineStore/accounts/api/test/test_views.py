from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from accounts.utils import generate_access_token, generate_refresh_token

User = get_user_model()


class TokenObtainPairViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_generate_tokens(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/token/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)

    def test_no_token_generated(self):
        response = self.client.get('/token/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'No Token Generated')

    def test_generate_tokens_unauthenticated(self):
        response = self.client.get('/token/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
