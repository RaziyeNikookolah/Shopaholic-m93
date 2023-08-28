from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from accounts.models import Account
from ..serializers import AccountSerializer

from datetime import timedelta


class ViewsTestCase(TestCase):

    def setUp(self):
        # access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJleHAiOjE2OTMyMDU5NjQsImlhdCI6MTY5MzIwNTc4NH0.weqCufxzcWAmC-6jG-7GDClUo_vXiHhbgYbfnIpZ6rk",
        # refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJleHAiOjE2OTU3OTc3ODQsImlhdCI6MTY5MzIwNTc4NH0.pApYvB-XMJlKv6CuyJqqQiyLUfyJnkUVOFCdmKJKW-g"
        self.client = APIClient()
        self.user = Account.objects.create(phone_number='1234567890')
        self.client.force_authenticate(user=self.user)

    def test_token_obtain_pair_view(self):
        url = reverse('optain_pair_tokens')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)

    def test_account_list_view(self):
        url = reverse('account-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = AccountSerializer(Account.objects.all(), many=True)
        self.assertEqual(response.data, serializer.data)

    def test_account_list_view_unauthenticated(self):
        self.client.logout()
        url = reverse('account-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
