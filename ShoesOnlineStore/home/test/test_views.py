from model_bakery import baker
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
# Import your models
from shoes.models import Brand, Product, Price, Color, Size, SHOES_SIZE_NAME
from shoes.serializer import ProductsSerializer  # Import your serializers


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.product = baker.make(Product)
        self.price = baker.make(Price, product=self.product)
        self.color = baker.make(Color)
        self.size = baker.make(Size, name=SHOES_SIZE_NAME.ADULT)
        self.product.color.add(self.color)
        self.product.size.add(self.size)

    def test_home_view(self):
        url = reverse('home:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'index.html')

    # def test_shop_single_view(self):
    #     url = reverse('home:shop_single', args=[self.product.pk])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertTemplateUsed(response, 'shop_single.html')
    #     self.assertIn('product', response.context)
    #     self.assertIn('sizes', response.context)
    #     self.assertIn('colors', response.context)

    def test_shoe_detail_view(self):
        url = reverse('home:shoe_detail', args=[self.product.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = ProductsSerializer(self.product)

    # def test_invalid_product_id_shop_single_view(self):
    #     invalid_product_id = 999  # A product ID that doesn't exist
    #     url = reverse('home:shop_single', args=[invalid_product_id])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_home_view(self):
        url = reverse('home:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'index.html')

    # def test_about_view(self):
    #     url = reverse('home:about')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertTemplateUsed(response, 'about.html')

    # def test_shop_view(self):
    #     url = reverse('home:shop')
    #     response = self.client.get(url)
    #     print("***************************************")
    #     print("*"*20, response, "*"*20)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertTemplateUsed(response, 'shop.html')

    def test_cart_view(self):
        url = reverse('home:cart')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'cart.html')

    # def test_invalid_product_id_shop_single_view(self):
    #     invalid_product_id = 999  # A product ID that doesn't exist
    #     url = reverse('home:shop_single', args=[invalid_product_id])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_checkout_view(self):
        url = reverse('home:checkout')
        response = self.client.get(url)
        # 401_UNAUTHORIZED)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'checkout.html')

    # def test_contact_view(self):
    #     url = reverse('home:contact')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertTemplateUsed(response, 'contact.html')

    def test_thankyou_view(self):
        url = reverse('home:thank_you')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'thankyou.html')

    # def test_invalid_shoe_detail_view(self):
    #     invalid_product_id = 999  # A product ID that doesn't exist
    #     url = reverse('home:shoe_detail', args=[invalid_product_id])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
