from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from shoes.models import Category, Color
from shoes.api.views import ListCategory, ListColor
from shoes.api.serializers import CategorySerializer, ColorSerializer
from django.urls import reverse
from rest_framework import status
import json


class CategoryColorAPITest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.category = Category.objects.create(title='Test Category')
        self.color = Color.objects.create(name='Red')

    def test_list_categories(self):
        url = reverse('category-list')
        request = self.factory.get(url)
        view = ListCategory.as_view({'get': 'list'})
        response = view(request)
        expected_data = CategorySerializer([self.category], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_list_colors(self):
        url = reverse('color-list')
        request = self.factory.get(url)
        view = ListColor.as_view({'get': 'list'})
        response = view(request)
        expected_data = ColorSerializer([self.color], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
