from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Product, Price, Brand, Category


class ProductListViewTest(APITestCase):
    def setUp(self):
        # Create test data
        self.product1 = Product.objects.create(
            title="Running Shoes", brand=Brand.objects.create(title="Nike"),
            code="ABC123", category=Category.objects.create(title="Footwear"),
            available_quantity=10
        )
        self.product2 = Product.objects.create(
            title="Sneakers", brand=Brand.objects.create(title="Adidas"),
            code="XYZ456", category=Category.objects.create(title="Footwear"),
            available_quantity=5
        )
        self.price1 = Price.objects.create(product=self.product1, price=100)
        self.price2 = Price.objects.create(product=self.product2, price=80)

    def test_product_list(self):
        url = reverse('product-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_product_list_with_search(self):
        url = reverse('product-list')
        data = {'search': 'Running'}
        response = self.client.get(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Running Shoes")

    def test_product_list_with_filters(self):
        url = reverse('product-list')
        data = {'brand__title': 'Nike', 'color__name': 'Red'}
        response = self.client.get(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Running Shoes")

    def test_product_list_caching(self):
        url = reverse('product-list')

        response1 = self.client.get(url)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

        # Modify data
        self.product1.available_quantity = 5
        self.product1.save()

        response2 = self.client.get(url)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

        self.assertEqual(response1.content, response2.content)
