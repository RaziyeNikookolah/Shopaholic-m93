
from django.urls import path
from . import views, zarrinpal_views


urlpatterns = [

    path("create/", views.OrderCreateView.as_view(), name="order_create"),
    path("cart_list/", views.CartListView.as_view(), name="cart_list"),
    path("add_to_cart/", views.AddToCartView.as_view(), name="add_to_cart"),
    path("remove_from_cart/", views.RemoveCartItemView.as_view(),
         name="remove_from_cart"),
    path("update_cart/", views.UpdateCartItemView.as_view(),
         name="update_cart"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    path("create_order/", views.CreateOrder.as_view(), name="create_order"),

    #     path('request_payment/', views.ZarrinPalRequestPayment.as_view(),
    #          name='request_payment'),
    #     path('verify_payment/', views.ZarrinPalVerifyPayment.as_view(),
    #          name='verify_payment'),

    #     path('request-payment/', zarinpal_views.request_payment, name='request_payment'),
    #     path('verify-payment/', zarinpal_views.verify_payment, name='verify_payment')
    path('request/', zarrinpal_views.send_request, name='request'),
    path('verify/', zarrinpal_views.verify, name='verify'),

]
