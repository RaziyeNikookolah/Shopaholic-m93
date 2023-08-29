from model_bakery import baker
from django.test import TestCase
from ..tasks import send_delivery_status_email, send_order_paid_email, email_export


class TaskTests(TestCase):

    def test_send_delivery_status_email(self):
        order = baker.make("orders.Order")  # Create a test Order instance
        result = send_delivery_status_email(order.id)
        # Verify the expected result message
        self.assertIn("Email sent to", result)

    def test_send_order_paid_email(self):
        order = baker.make("orders.Order")  # Create a test Order instance
        result = send_order_paid_email(order.id)
        # Verify the expected result message
        self.assertIn("Email sent to", result)

    def test_email_export(self):
        baker.make("orders.Order")  # Create some test Order instances
        result = email_export()
        # Verify the expected result message
        self.assertIn("Exported orders to", result)


class OrderModelTests(TestCase):

    def test_save_send_delivery_status_email(self):
        # Create a test Order instance with delivery_status = 2
        order = baker.make("orders.Order")
        order.delivery_status = 2
        order.save()

    def test_save_send_order_paid_email(self):
        # Create a test Order instance with is_paid = True
        order = baker.make("orders.Order")
        order.is_paid = True
        order.save()
