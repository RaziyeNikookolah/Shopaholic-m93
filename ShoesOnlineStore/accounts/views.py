from celery.schedules import crontab
from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from .tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django.shortcuts import render
from django.views import View
from django.contrib.auth import logout
from rest_framework.views import APIView


class LoginView(View):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        # form = UserRegiterOrLoginForm()
        return render(request, self.template_name)


class LogoutView(View):
    template_name = "logout.html"

    def get(self, request, *args, **kwargs):
        # form = UserRegiterOrLoginForm()
        return render(request, self.template_name)


class RequestLogoutView(APIView):
    template_name = "logout.html"

    def get(self, request, *args, **kwargs):
        logout(request)


def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(
        hour=1, minute=34)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_" +
                                       "5", task='send_mail_app.tasks.send_mail_func')  # , args = json.dumps([[2,3]]))
    return HttpResponse("Done")
