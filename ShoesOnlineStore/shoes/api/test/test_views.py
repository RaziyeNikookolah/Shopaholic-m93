from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from shoes.models import Category, Color
from shoes.api.serializers import CategorySerializer, ColorSerializer


class ListCategoryAndColorViewsetTest(APITestCase):
    def setUp(self):
        self.category1 = Category.objects.create(title="Footwear")
        self.category2 = Category.objects.create(title="Apparel")

        self.color1 = Color.objects.create(name="Red")
        self.color2 = Color.objects.create(name="Blue")

    def test_list_categories(self):
        url = reverse('category-list')  # Replace with actual URL name
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_colors(self):
        url = reverse('color-list')  # Replace with actual URL name
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_categories_with_serializer(self):
        serializer = CategorySerializer(
            [self.category1, self.category2], many=True)
        url = reverse('category-list')  # Replace with actual URL name
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_colors_with_serializer(self):
        serializer = ColorSerializer([self.color1, self.color2], many=True)
        url = reverse('color-list')  # Replace with actual URL name
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
