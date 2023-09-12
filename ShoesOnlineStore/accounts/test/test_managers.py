from django.test import TestCase
from django.contrib.auth import get_user_model
from core.utils import ROLE
from ..models import Customer


User = get_user_model()


class AccountManagerTests(TestCase):

    def test_create_user(self):
        account = User.objects.create_user(
            phone_number="1234567890"
        )
        self.assertIsNotNone(account)
        self.assertFalse(account.is_staff)
        self.assertFalse(account.is_superuser)
        self.assertTrue(account.is_active)
        self.assertEqual(account.role, ROLE.USER)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            phone_number="9876543210"
        )
        self.assertIsNotNone(superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)
        self.assertEqual(superuser.role, ROLE.MANAGER)


class CustomerManagerTests(TestCase):

    def test_get_queryset(self):
        User.objects.create_user(
            phone_number="1234567890", role=ROLE.CUSTOMER
        )
        User.objects.create_user(
            phone_number="9876543210", role=ROLE.MANAGER
        )

        customers = Customer.objects.all()
        self.assertEqual(customers.count(), 1)
        self.assertEqual(customers[0].role, ROLE.CUSTOMER)
