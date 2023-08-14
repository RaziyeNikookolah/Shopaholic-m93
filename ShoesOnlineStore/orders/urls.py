
from django.urls import path
from . import views


urlpatterns = [

    path("create/", views.OrderCreateView.as_view(), name="order_create"),
    path("cart_list/", views.CartListView.as_view(), name="cart_list"),
    path("add_to_cart/", views.AddToCartView.as_view(), name="add_to_cart"),
    path("remove_from_cart/", views.RemoveCartItemView.as_view(),
         name="remove_from_cart"),
    path("update_cart/", views.UpdateCartItemView.as_view(),
         name="update_cart"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),

    # path('request_payment/', views.request_payment, name='request_payment'),
    # path('verify_payment/', views.verify_payment, name='verify_payment'),
]
