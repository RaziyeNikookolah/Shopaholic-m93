from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    # path('', views.getRoutes, name='routes'),


]
