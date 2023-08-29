from django.test import TestCase
from django.urls import reverse
from accounts.models import Account
from orders.models import Order
from rest_framework.test import APIClient


class PaymentViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Account.objects.create(phone_number='1234567890')
        self.client.force_authenticate(user=self.user)

        # Create a sample order
        self.order = Order.objects.create(
            account=self.user, is_paid=False)

    def test_payment_request_view(self):
        response = self.client.get(
            reverse('request', args=[self.order.id]))

        self.assertEqual(response.status_code, 200)  # Expecting a redirect

    def test_payment_verify_view(self):
        session = self.client.session
        session['order_payment'] = {"order_id": self.order.id}
        session.save()
        self.order.is_paid = True
        self.order.save()

        response = self.client.get(
            reverse('verify'), {'authority': '000000000000000000000000000001200267', 'Status': 'OK'})

        # The response status should be 200 for a successful verification
        self.assertEqual(response.status_code, 200)

        # The response content should contain the success message

    def tearDown(self):
        self.client.logout()
