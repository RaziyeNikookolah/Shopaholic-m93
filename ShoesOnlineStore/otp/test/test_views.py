from django.urls import reverse
from django.test import TestCase, Client
from otp.models import OtpRequest
from ..views import RequestOTP, VerifyOtp


class OtpViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_request_otp(self):
        request_data = {'phone_number': '9876543210'}
        url = reverse('otp_request')
        response = self.client.post(url, request_data)
        self.assertEqual(response.status_code, 500)

    def test_verify_otp(self):
        otp_request = OtpRequest.objects.create(phone_number='9876543210')
        otp_request.generate_code()
        otp_request.save()

        # Login the user
        self.client.login(phone_number='9876543210', password='testpassword')

        request_data = {'phone_number': '9876543210', 'code': otp_request.code}
        url = reverse('otp_verify')
        response = self.client.post(url, request_data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_verify_otp(self):
        # Login the user
        self.client.login(phone_number='9876543210')

        request_data = {'phone_number': '9876543210', 'code': '1234'}
        url = reverse('otp_verify')

        response = self.client.post(url, request_data)
        self.assertEqual(response.status_code, 400)
