from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("request_logout/", views.RequestLogoutView.as_view(), name="request_logout"),
    path("send_email_to_all/", views.send_mail_to_all, name="send_email_to_all"),
    path('', views.test, name="test"),
    path('sendmail/', views.send_mail_to_all, name="sendmail"),
    path('schedulemail/', views.schedule_mail, name="schedulemail"),
]
