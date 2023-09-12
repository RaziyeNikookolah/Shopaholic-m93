import unittest
from django.urls import reverse, resolve
from .. import views


class TestUrls(unittest.TestCase):
    def test_product_list_url(self):
        url = reverse('product_list')
        self.assertEqual(resolve(url).func.view_class, views.ProductList)

    def test_product_details_url(self):
        # Assuming pk = 1 for testing purposes
        url = reverse('product_details', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.ProductDetails)


if __name__ == '__main__':
    unittest.main()
