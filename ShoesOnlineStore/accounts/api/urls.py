from django.urls import path
from . import views


urlpatterns = [
    path('access_token/', views.AccessTokenView.as_view(), name="access_token"),
    path('refresh_token/', views.RefreshTokenView.as_view(), name="refresh_token"),

]
