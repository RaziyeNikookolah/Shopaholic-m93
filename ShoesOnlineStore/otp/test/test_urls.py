import unittest
from django.urls import reverse, resolve
from .. import views


class TestUrls(unittest.TestCase):
    def test_request_otp_url(self):
        url = reverse('otp_request')
        self.assertEqual(resolve(url).func.view_class, views.RequestOTP)

    def test_verify_otp_url(self):
        url = reverse('otp_verify')
        self.assertEqual(resolve(url).func.view_class, views.VerifyOtp)


if __name__ == '__main__':
    unittest.main()
