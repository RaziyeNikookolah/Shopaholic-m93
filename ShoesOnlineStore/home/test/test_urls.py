import unittest
from django.urls import reverse, resolve
from .. import views


class TestUrls(unittest.TestCase):
    def test_index_url(self):
        url = reverse('home:index')
        self.assertEqual(resolve(url).func.view_class, views.HomeView)

    def test_about_url(self):
        url = reverse('home:about')
        self.assertEqual(resolve(url).func.view_class, views.AboutView)

    def test_cart_url(self):
        url = reverse('home:cart')
        self.assertEqual(resolve(url).func.view_class, views.CartView)

    def test_contact_url(self):
        url = reverse('home:contact')
        self.assertEqual(resolve(url).func.view_class, views.ContactView)

    def test_shop_url(self):
        url = reverse('home:shop')
        self.assertEqual(resolve(url).func.view_class, views.ShopView)

    def test_shop_single_url(self):
        # Assuming pk = 1 for testing purposes
        url = reverse('home:shop_single', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.ShopSingleView)

    def test_thank_you_url(self):
        url = reverse('home:thank_you')
        self.assertEqual(resolve(url).func.view_class, views.ThankyouView)

    def test_checkout_url(self):
        url = reverse('home:checkout')
        self.assertEqual(resolve(url).func.view_class, views.CheckoutView)

    def test_shoe_detail_url(self):
        # Assuming pk = 1 for testing purposes
        url = reverse('home:shoe_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.ShoeDetail)


if __name__ == '__main__':
    unittest.main()
