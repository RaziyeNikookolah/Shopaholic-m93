import unittest
from django.urls import reverse, resolve
from rest_framework import routers
from accounts.api.views import router as accounts_router
from .. import views


class TestUrls(unittest.TestCase):
    def test_token_obtain_pair_url(self):
        url = reverse('optain_pair_tokens')
        self.assertEqual(resolve(url).func.view_class,
                         views.TokenObtainPairView)

    # def test_accounts_router_urls(self):
    #     account_urls = accounts_router.urls
    #     for url_pattern in account_urls:
    #         url_name = getattr(url_pattern, 'name', None)
    #         if url_name:
    #             url = reverse(url_name)
    #             resolved_func = resolve(url).func
    #             expected_view_class_name = url_name.capitalize() + 'View'
    #             expected_view_class = getattr(
    #                 views, expected_view_class_name, None)
    #             if expected_view_class:
    #                 self.assertEqual(resolved_func.__class__,
    #                                  expected_view_class)


if __name__ == '__main__':
    unittest.main()
