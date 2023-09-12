from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from model_bakery import baker
from accounts.models import Account
from accounts.backends import PhoneNumberBackend


class PhoneNumberBackendTests(TestCase):

    def setUp(self):
        self.backend = PhoneNumberBackend()
        self.user_data = {
            'phone_number': '1234567890',
            'password': 'testpassword',
        }
        self.user = baker.make(Account, **self.user_data)
        self.user.set_password(self.user_data['password'])
        self.user.save()

    def test_authenticate_valid_credentials(self):
        user = self.backend.authenticate(
            None, username=self.user_data['phone_number'], password=self.user_data['password']
        )
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)

    def test_authenticate_invalid_username(self):
        user = self.backend.authenticate(
            None, username='invalid_username', password=self.user_data['password']
        )
        self.assertIsNone(user)

    def test_authenticate_invalid_password(self):
        user = self.backend.authenticate(
            None, username=self.user_data['phone_number'], password='invalid_password'
        )
        self.assertIsNone(user)

    def test_get_user_valid_user_id(self):
        user = self.backend.get_user(self.user.id)
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)

    def test_get_user_invalid_user_id(self):
        user = self.backend.get_user(self.user.id + 1)
        self.assertIsNone(user)
