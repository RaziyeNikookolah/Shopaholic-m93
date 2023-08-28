import unittest
from django.urls import reverse, resolve
from .. import views, zarinpal_views


class TestUrls(unittest.TestCase):
    def test_cart_list_url(self):
        url = reverse('cart_list')
        self.assertEqual(resolve(url).func.view_class, views.CartListView)

    # def test_add_to_cart_url(self):
    #     url = reverse('add_to_cart')
    #     self.assertEqual(resolve(url).func.view_class, views.AddToCartView)

    # def test_remove_from_cart_url(self):
    #     url = reverse('remove_from_cart')
    #     self.assertEqual(resolve(url).func.view_class,
    #                      views.RemoveCartItemView)

    def test_update_cart_url(self):
        url = reverse('update_cart')
        self.assertEqual(resolve(url).func.view_class,
                         views.UpdateCartItemView)

    def test_checkout_url(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func.view_class, views.CheckoutView)

    def test_create_order_url(self):
        url = reverse('create_order')
        self.assertEqual(resolve(url).func.view_class, views.CreateOrder)

    def test_payment_request_url(self):
        # Assuming order_id = 1 for testing purposes
        url = reverse('request', args=[1])
        self.assertEqual(resolve(url).func.view_class,
                         zarinpal_views.PaymentRequest)

    def test_payment_verify_url(self):
        url = reverse('verify')
        self.assertEqual(resolve(url).func.view_class,
                         zarinpal_views.PaymentVerify)


if __name__ == '__main__':
    unittest.main()
