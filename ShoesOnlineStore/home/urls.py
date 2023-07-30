from django.contrib import admin
from django.urls import path
from . import views


# Django admin customization

admin.site.site_title = "Welcome to Shoes Online Shop"
admin.site.index_title = "Welcome to Shoes Online Shop"


urlpatterns = [
    path("index/", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
]
