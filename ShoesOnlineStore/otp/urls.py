from django.urls import path
from . import views

urlpatterns = [
    path('request_otp/', views.RequestOTP.as_view(), name="otp_request"),
    path('verify_otp/', views.VerifyOtp.as_view(), name="otp_verify"),

]
