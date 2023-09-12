from django.test import TestCase
from django.contrib.sessions.backends.db import SessionStore
from model_bakery import baker
from decimal import Decimal
from accounts.models import Account as User
from orders.models import Order, OrderItem
from shoes.models import SHOES_SIZE_NAME, Price, Product, Size
from orders.utils import (
    remove_product_from_session,
    add_product_to_session,
    session_cart,
    session_key,
    create_orderItems_from_session,
)


class CartUtilsTests(TestCase):

    def setUp(self):
        self.user = baker.make(User, phone_number="09876543")
        self.product = baker.make(
            Product)
        self.price = baker.make(Price, product=self.product)
        self.size = baker.make(Size, name=SHOES_SIZE_NAME.ADULT)
        self.product.size.add(self.size)

    def test_remove_product_from_session(self):
        session = SessionStore()
        session[session_key] = {str(self.product.id): {}}
        session.save()
        response = remove_product_from_session(self.product.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": 'Empty cart'})

    def test_remove_product_from_session_empty_cart(self):
        session = SessionStore()
        response = remove_product_from_session(self.product.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": 'Empty cart'})
