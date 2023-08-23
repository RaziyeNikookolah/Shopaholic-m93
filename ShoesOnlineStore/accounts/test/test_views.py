from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from ..views import LoginView, LogoutView, RequestLogoutView, test, send_mail_to_all, schedule_mail


class LoginViewTest(TestCase):
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


class LogoutViewTest(TestCase):
    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logout.html')


class RequestLogoutViewTest(TestCase):
    def test_request_logout_view(self):
        request = RequestFactory().get('/')
        request.user = User()
        response = RequestLogoutView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, HttpResponse)


class TestViewTest(TestCase):
    def test_test_view(self):
        response = self.client.get(reverse('test'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Done")


class SendMailToAllViewTest(TestCase):
    def test_send_mail_to_all_view(self):
        response = self.client.get(reverse('send_mail_to_all'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Sent")


class ScheduleMailViewTest(TestCase):
    def test_schedule_mail_view(self):
        response = self.client.get(reverse('schedule_mail'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Done")
