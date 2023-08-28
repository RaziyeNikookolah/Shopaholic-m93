import unittest
from django.urls import reverse, resolve
from .. import views


class TestUrls(unittest.TestCase):
    def test_profile_url(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func.view_class, views.ProfileView)

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, views.LoginView)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, views.LogoutView)

    def test_request_logout_url(self):
        url = reverse('request_logout')
        self.assertEqual(resolve(url).func.view_class, views.RequestLogoutView)


if __name__ == '__main__':
    unittest.main()
