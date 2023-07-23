from django.urls import path
from . import views

urlpatterns = [
    path('request_otp/', views.RequestOTP.as_view()),
    path('verify_otp/', views.VerifyOtp.as_view()),

]
