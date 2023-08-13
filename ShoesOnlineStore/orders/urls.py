from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path("create/", views.order_create, name="order_create"),
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("remove_from_cart/", views.remove_from_cart, name="remove_from_cart"),
    path("cart_list/", views.cart_list, name="cart_list"),
    # path('request_payment/', views.request_payment, name='request_payment'),
    # path('verify_payment/', views.verify_payment, name='verify_payment'),
]
