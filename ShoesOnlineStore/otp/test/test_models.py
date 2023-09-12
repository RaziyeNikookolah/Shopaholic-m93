from django.test import TestCase
from datetime import datetime, timedelta, timezone
from ..models import OtpRequest


class OtpRequestModelTest(TestCase):
    def setUp(self):
        self.otp_request = OtpRequest.objects.create(
            phone_number='+1234567890')

    def test_generate_code(self):
        self.otp_request.generate_code()
        self.assertIsNotNone(self.otp_request.code)
        self.assertEqual(len(self.otp_request.code), 4)

    def test_is_expired(self):
        # Test when the OTP is not expired
        self.otp_request.valid_until = datetime.now(
            timezone.utc) + timedelta(seconds=120)
        self.assertFalse(self.otp_request.is_expired())

        # Test when the OTP is expired
        self.otp_request.valid_until = datetime.now(
            timezone.utc) - timedelta(seconds=120)
        self.assertTrue(self.otp_request.is_expired())

    def test_random_code_generation(self):
        code = self.otp_request._random_code()
        self.assertIsNotNone(code)
        self.assertEqual(len(code), 4)
        self.assertTrue(code.isdigit())

# Add more test cases as needed
