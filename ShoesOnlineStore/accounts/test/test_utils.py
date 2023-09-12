from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from accounts.utils import generate_access_token, generate_refresh_token

User = get_user_model()


class TokenGenerationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            phone_number="111111111"
        )

    def test_generate_access_token(self):
        access_token = generate_access_token(
            self.user, expiration_time_minutes=30)
        self.assertIsNotNone(access_token)

        # Decode the access token and verify its payload
        decoded_payload = jwt.decode(
            access_token, settings.SECRET_KEY, algorithms=["HS256"])
        self.assertEqual(decoded_payload["user_id"], self.user.id)

    def test_generate_refresh_token(self):
        refresh_token = generate_refresh_token(
            self.user, expiration_time_days=7)
        self.assertIsNotNone(refresh_token)

        # Decode the refresh token and verify its payload
        decoded_payload = jwt.decode(
            refresh_token, settings.SECRET_KEY, algorithms=["HS256"])
        self.assertEqual(decoded_payload["user_id"], self.user.id)
