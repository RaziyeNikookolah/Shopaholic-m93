from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from ..models import Account, Profile, Address, Customer
from core.utils import ROLE


class AccountModelTest(TestCase):
    def test_create_account(self):
        account = Account.objects.create(
            phone_number='12345678901', role=ROLE.USER)

        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(account.get_full_name(), 'Anonymous')
        self.assertEqual(
            str(account), f"User with phone number:{account.phone_number}")
        self.assertEqual(account.role, ROLE.USER)
        self.assertFalse(account.is_active)
        self.assertFalse(account.is_staff)
        self.assertFalse(account.is_superuser)


class ProfileModelTest(TestCase):
    def test_create_profile(self):
        account = Account.objects.create(
            phone_number='12345678901', role=ROLE.USER)
        profile = Profile.objects.create(
            account=account,
            first_name='John',
            last_name='Doe',
            gender=Profile.GENDER.MALE,
            birthday=timezone.now(),
            bio='A short bio about me',
            email='john@example.com'
        )

        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(str(profile), f'Profile for John Doe')
        self.assertEqual(profile.account, account)
        self.assertEqual(profile.get_gender_display(), 'Male')


class AddressModelTest(TestCase):
    def test_create_address(self):
        account = Account.objects.create(
            phone_number='12345678901', role=ROLE.USER)
        address = Address.objects.create(
            account=account,
            province='Tehran',
            city='Tehran',
            address='123 Main St',
            postal_code='12345'
        )

        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(str(address), f' Iran, Tehran, Tehran, 123 Main St')


class CustomerModelTest(TestCase):
    def test_create_customer(self):
        customer = Customer.objects.create(
            phone_number='12345678901', role=ROLE.CUSTOMER)

        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(customer.get_full_name(), 'Anonymous')
        self.assertEqual(
            str(customer), f"User with phone number:{customer.phone_number}")
        self.assertEqual(customer.role, ROLE.CUSTOMER)
        self.assertFalse(customer.is_active)
        self.assertFalse(customer.is_staff)
        self.assertFalse(customer.is_superuser)
