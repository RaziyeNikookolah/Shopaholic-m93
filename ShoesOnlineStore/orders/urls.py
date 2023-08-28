
from django.urls import path
from . import views, zarinpal_views


urlpatterns = [

    path("cart_list/", views.CartListView.as_view(), name="cart_list"),
    path("add_to_cart/", views.AddToCartView.as_view(), name="add_to_cart"),
    #     path("remove_from_cart/", views.RemoveCartItemView.as_view(),
    #     name="remove_from_cart"),
    path("update_cart/", views.UpdateCartItemView.as_view(),
         name="update_cart"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    path("create_order/", views.CreateOrder.as_view(), name="create_order"),

    path('request/<int:order_id>/',
         zarinpal_views.PaymentRequest.as_view(), name='request'),
    path('verify/', zarinpal_views.PaymentVerify.as_view(), name='verify'),

]
