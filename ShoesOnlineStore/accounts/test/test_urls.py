from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse
from ..views import LoginView, LogoutView, RequestLogoutView, test, send_mail_to_all, schedule_mail


class UrlsTest(TestCase):
    def test_login_url(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, '<form')

    def test_logout_url(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logout.html')
        self.assertContains(response, '<h1>Logout</h1>')

    def test_request_logout_url(self):
        url = reverse('request_logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, HttpResponse)

    def test_send_email_to_all_url(self):
        url = reverse('send_email_to_all')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Sent")

    def test_test_url(self):
        url = reverse('test')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Done")

    def test_sendmail_url(self):
        url = reverse('sendmail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Sent")

    def test_schedulemail_url(self):
        url = reverse('schedulemail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Done")
