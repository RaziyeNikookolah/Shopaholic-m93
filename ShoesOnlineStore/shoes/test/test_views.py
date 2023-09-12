from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase


class ProductListViewTestCase(APITestCase):
    def test_product_list(self):
        # it makes 2 with product _quantity=2
        product = baker.make('Product', _quantity=2)

        url = reverse('product_list')  # Make sure to use the actual URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProductDetailsViewTestCase(APITestCase):
    def test_product_details(self):
        product = baker.make(
            'Product', title='Test Product', available_quantity=3)

        url = reverse('product_details', args=[
                      product.id])  # Use the correct ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Product')

    def test_product_details_not_found(self):
        url = reverse('product_details', args=[999])  # Non-existent product ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
