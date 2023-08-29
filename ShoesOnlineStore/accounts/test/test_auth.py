import jwt
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from unittest.mock import Mock
from rest_framework.exceptions import AuthenticationFailed
from accounts.authentication import JWTAuthentication, LoginAuthentication

User = get_user_model()


class JWTAuthenticationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            phone_number="122228787"
        )
        self.token_payload = {"user_id": self.user.id}
        self.jwt_token = jwt.encode(
            self.token_payload, settings.SECRET_KEY, algorithm="HS256"
        )

    def test_authenticate_valid_token(self):
        request = Mock()
        request.headers.get.return_value = f"Bearer {self.jwt_token}"

        auth = JWTAuthentication()
        user, payload = auth.authenticate(request)

        self.assertEqual(user, self.user)
        self.assertEqual(payload, self.token_payload)

    def test_authenticate_missing_token(self):
        request = Mock()
        request.headers.get.return_value = None

        auth = JWTAuthentication()
        with self.assertRaises(AuthenticationFailed):
            auth.authenticate(request)


class LoginAuthenticationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            phone_number="12336677"
        )
        self.token_payload = {"user_id": self.user.id}
        self.jwt_token = jwt.encode(
            self.token_payload, settings.SECRET_KEY, algorithm="HS256"
        )

    def test_authenticate_valid_token(self):
        request = Mock()
        request.headers.get.return_value = f"Bearer {self.jwt_token}"

        auth = LoginAuthentication()
        user, payload = auth.authenticate(request)

        self.assertEqual(user, self.user)
        self.assertEqual(payload, self.token_payload)

    def test_authenticate_missing_token(self):
        request = Mock()
        request.headers.get.return_value = None

        auth = LoginAuthentication()
        result = auth.authenticate(request)

        self.assertIsNone(result)
