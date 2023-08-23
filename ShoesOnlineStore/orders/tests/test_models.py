from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Account
from shoes.models import Product, Price
from ..models import Order, OrderItem, Receipt

User = get_user_model()


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.account = Account.objects.create(user=self.user)
        self.product = Product.objects.create(name='Test Product')
        self.order = Order.objects.create(account=self.account)

    def test_get_total_price(self):
        order_item = OrderItem.objects.create(
            order=self.order, product=self.product, quantity=2
        )
        price = Price.objects.create(product=self.product, price=100)
        expected_total_price = price.price * order_item.quantity
        self.assertEqual(self.order.get_total_price(), expected_total_price)

    def test_order_str_representation(self):
        self.assertEqual(
            str(self.order), f"Order id:{self.order.id}"
        )


class OrderItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.account = Account.objects.create(user=self.user)
        self.product = Product.objects.create(name='Test Product')
        self.order = Order.objects.create(account=self.account)

    def test_get_cost(self):
        order_item = OrderItem.objects.create(
            order=self.order, product=self.product, quantity=3
        )
        price = Price.objects.create(product=self.product, price=50)
        expected_cost = price.price * order_item.quantity
        self.assertEqual(order_item.get_cost(), expected_cost)

    def test_order_item_str_representation(self):
        order_item = OrderItem.objects.create(
            order=self.order, product=self.product, quantity=3
        )
        self.assertEqual(
            str(order_item), f"{order_item.product} {order_item.order}"
        )


class ReceiptModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.account = Account.objects.create(user=self.user)
        self.product = Product.objects.create(name='Test Product')
        self.order = Order.objects.create(account=self.account)
        self.price = Price.objects.create(product=self.product, price=50)

    def test_receipt_str_representation(self):
        receipt = Receipt.objects.create(
            order=self.order,
            total_price=self.price.price * 3,
            final_price=self.price.price * 3,
        )
        self.assertEqual(
            str(receipt), f"{receipt.final_price}"
        )
