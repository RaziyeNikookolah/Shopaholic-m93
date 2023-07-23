from django.urls import path
from .views import RequestOTP, VerifyOtp

urlpatterns = [
    path('request_otp/', RequestOTP.as_view()),
    path('verify_otp/', VerifyOtp.as_view()),

]
