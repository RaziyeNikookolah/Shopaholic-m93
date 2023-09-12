from django.test import TestCase
from model_bakery import baker

from shoes.models import Price, Product
from ..models import Order, OrderItem, Receipt
from accounts.models import Account
from core.utils import PROVINCES
from datetime import datetime
from unittest.mock import patch


class OrderModelsTestCase(TestCase):

    def setUp(self):
        self.product1 = baker.make(Product)
        self.product2 = baker.make(Product)
        self.price1 = baker.make(Price, product=self.product1, price=100)
        self.price2 = baker.make(Price, product=self.product2, price=100)
        self.account = baker.make(Account)
        self.order = baker.make(Order, account=self.account)
        self.orderItem1 = baker.make(
            OrderItem, order=self.order, product=self.product1)
        self.orderItem2 = baker.make(
            OrderItem, order=self.order, product=self.product2)

    def test_order_str(self):
        self.assertEqual(str(self.order), f"Order id:{self.order.id}")

    @patch('orders.models.OrderItem.get_cost')
    def test_get_total_price(self, mock_get_cost):
        mock_get_cost.return_value = 100  # Set the mock return value
        items = baker.make(OrderItem, _quantity=3, order=self.order)
        self.assertEqual(self.order.get_total_price(), 500)  # 100 * 3

    def test_send_delivery_status_email_on_save(self):
        self.order.delivery_status = Order.DeliveryStatus.SENT
        self.order.save()

        # You should check whether the email was actually sent in a real test environment

    def test_send_order_paid_email_on_save(self):
        self.order.is_paid = True
        self.order.save()

        # You should check whether the email was actually sent in a real test environment


class OrderItemModelTestCase(TestCase):

    def get_cost(self):
        last_price_query = Price.objects.filter(product=self.product).order_by(
            '-create_timestamp').values('price')[:1]

        print("Last price query:", last_price_query)

        if last_price_query:
            last_price = last_price_query[0]['price']
            print("Last price:", last_price)
            return last_price * self.quantity
        else:
            return 0


class ReceiptModelTestCase(TestCase):

    def setUp(self):
        self.product = baker.make(Product)
        self.price = baker.make(Price, product=self.product, price=100)
        self.account = baker.make(Account)
        self.order = baker.make(Order, account=self.account)
        self.order_item = baker.make(
            OrderItem, order=self.order, product=self.product)
        self.receipt = baker.make(
            Receipt,
            order=self.order,
            total_price=self.order.get_total_price(),
            final_price=self.order.get_total_price(),
        )

    def test_receipt_str(self):
        self.assertEqual(str(self.receipt), str(self.receipt.final_price))
