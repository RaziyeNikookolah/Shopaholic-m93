from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import OtpRequest
from ..utils import send_otp_request, verify_otp_request


class OTPViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_request_otp(self):
        data = {'phone_number': '+1234567890'}
        response = self.client.post('/request-otp/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('otp_request_id', response.data)

    def test_verify_valid_otp(self):
        otp_request = OtpRequest.objects.create(phone_number='+1234567890')
        otp_request.generate_code()
        otp_request.save()
        data = {'phone_number': '+1234567890', 'code': otp_request.code}
        response = self.client.post('/verify-otp/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)

    def test_verify_invalid_otp(self):
        otp_request = OtpRequest.objects.create(phone_number='+1234567890')
        otp_request.generate_code()
        otp_request.save()
        data = {'phone_number': '+1234567890', 'code': '1234'}  # Invalid code
        response = self.client.post('/verify-otp/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid data provided.')

    def test_verify_missing_otp_request(self):
        data = {'phone_number': '+1234567890', 'code': '1234'}
        response = self.client.post('/verify-otp/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid data provided.')

# Add more test cases as needed
