from django.urls import path
from . import views


urlpatterns = [
    path('access_token/', views.AccessTokenView.as_view(), name="access_token"),
    path('refresh_token/', views.RefreshTokenView.as_view(), name="refresh_token"),
    path('optain_pair_tokens/', views.TokenObtainPairView.as_view(),
         name="optain_pair_tokens"),

]
# api/v1/accounts/access_token/
# api/v1/accounts/refresh_token/
# api/v1/accounts/optain_pair_tokens/
