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

# View for rendering the login page


class LoginView(View):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        # TODO: Handle form logic if needed
        return render(request, self.template_name)

# View for rendering the logout page


class LogoutView(View):
    template_name = "logout.html"

    def get(self, request, *args, **kwargs):
        # TODO: Handle form logic if needed
        return render(request, self.template_name)

# API view for handling user logout requests


class RequestLogoutView(APIView):
    def get(self, request, *args, **kwargs):
        # Log out the user
        logout(request)

# Trigger a test Celery task when this view is accessed


def test(request):
    test_func.delay()
    return HttpResponse("Done")

# Trigger a send email Celery task when this view is accessed


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")

# Schedule a periodic email sending task using Django Celery Beat


def schedule_mail(request):
    # Create or get an hourly and minute-based schedule
    schedule, created = CrontabSchedule.objects.get_or_create(
        hour=1, minute=34)  # Set the desired schedule time
    # Create a periodic task using the created schedule and Celery task
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_" +
                                       "5", task='send_mail_app.tasks.send_mail_func')  # Replace with your actual task path
    return HttpResponse("Done")
