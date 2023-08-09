from django.contrib import admin
from django.urls import path
from . import views


# Django admin customization

admin.site.site_title = "Welcome to Shoes Online Shop"
admin.site.index_title = "Welcome to Shoes Online Shop"

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("cart/", views.CartView.as_view(), name="cart"),
    path("cart/", views.CartView.as_view(), name="cart"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("shop/", views.ShopView.as_view(), name="shop"),
    path("shop_single/<int:pk>/", views.ShopSingleView.as_view(), name="shop_single"),
    path("thank_you/", views.ThankyouView.as_view(), name="thank_you"),
    path("cart/checkout/", views.CheckoutView.as_view(), name="checkout"),
    path("shoe_detail/<int:pk>/", views.ShoeDetail.as_view(), name="shoe_detail"),

]
