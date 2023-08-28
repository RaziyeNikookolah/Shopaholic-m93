from datetime import datetime
from django.test import TestCase
from model_bakery import baker
from ..models import Account, Profile, Wishes, Address
from core.utils import ROLE, PROVINCES
from shoes.models import Product
from django.utils.translation import gettext_lazy as _


class ModelsTestCase(TestCase):

    def test_create_account(self):
        account = baker.make(
            Account, phone_number="1234567890", role=ROLE.USER)
        self.assertEqual(account.phone_number, "1234567890")
        self.assertEqual(account.role, ROLE.USER)
        self.assertFalse(account.is_staff)
        self.assertFalse(account.is_active)
        self.assertFalse(account.is_superuser)
        self.assertEqual(
            str(account), f"User with phone number:{account.phone_number}")

    def test_create_profile(self):
        account = baker.make(Account, phone_number="1234567890")
        profile = baker.make(Profile,
                             create_timestamp=datetime.now(),
                             account=account,
                             first_name="John",
                             last_name="Doe",
                             gender=Profile.GENDER.MALE,
                             birthday="1990-01-01",
                             bio="Sample bio",
                             email="john@example.com",
                             card_shaba_number="1234567890123456"
                             )
        self.assertEqual(profile.account, account)
        self.assertEqual(profile.first_name, "John")
        self.assertEqual(profile.last_name, "Doe")
        self.assertEqual(profile.gender, Profile.GENDER.MALE)
        self.assertEqual(
            str(profile), f'Profile for {profile.first_name} {profile.last_name}')

    def test_create_wishes(self):
        product = baker.make(Product)
        account = baker.make(Account, phone_number="1234567890")
        wish = baker.make(Wishes,
                          account=account,
                          product=product,
                          product_clicked_count=5
                          )
        self.assertEqual(wish.account, account)
        self.assertEqual(wish.product, product)
        self.assertEqual(wish.product_clicked_count, 5)

    def test_create_address(self):

        account = baker.make(Account, phone_number="1234567890")
        address = baker.make(Address,
                             account=account,
                             province=PROVINCES[0][0],
                             city="Sample City",
                             address="123 Main St",
                             postal_code="12345"
                             )
        self.assertEqual(address.account, account)
        self.assertEqual(address.province, PROVINCES[0][0])
        self.assertEqual(address.city, "Sample City")
        self.assertEqual(address.address, "123 Main St")
        self.assertEqual(address.postal_code, "12345")

    def test_account_str(self):
        account = baker.make(Account, phone_number="123456789")
        self.assertEqual(str(account), f"User with phone number:123456789")

    def test_fullname_with_names(self):
        profile = baker.make(Profile,
                             first_name="John",
                             last_name="Doe",
                             create_timestamp=datetime.now())
        full_name = profile.fullname()
        self.assertEqual(full_name, "John Doe")

    def test_fullname_without_names(self):
        profile = baker.make(Profile,
                             create_timestamp=datetime.now())
        full_name = profile.fullname()
        self.assertEqual(full_name, "Anonymous")

    def test_fullname_with_first_name(self):
        profile = baker.make(Profile, last_name="", first_name="Alice",
                             create_timestamp=datetime.now())
        full_name = profile.fullname()
        self.assertEqual(full_name, "Alice ")

    def test_fullname_with_last_name(self):
        profile = baker.make(Profile, first_name="", last_name="Smith",
                             create_timestamp=datetime.now())
        full_name = profile.fullname()
        self.assertEqual(full_name, " Smith")

    def test_fullname_with_non_ascii_names(self):
        profile = baker.make(Profile,
                             first_name="محمد",
                             last_name="علی",
                             create_timestamp=datetime.now())
        full_name = profile.fullname()
        self.assertEqual(full_name, "محمد علی")

    def test_fullname_without_names(self):
        # Create an Account instance without first_name and last_name
        profile = baker.make(Profile, first_name="", last_name="",
                             create_timestamp=datetime.now())

        # Call the fullname method
        full_name = profile.fullname()

        # Check if the fullname is 'Anonymous'
        self.assertEqual(full_name, "Anonymous")

    def test_address_str(self):
        account = baker.make(Account)
        address = baker.make(Address,
                             account=account,
                             province=PROVINCES[0][0],
                             city="Sample City",
                             address="123 Main St",
                             postal_code="12345"
                             )
        self.assertEqual(
            str(address), f'{address.province}, {address.city}, {address.address}')
