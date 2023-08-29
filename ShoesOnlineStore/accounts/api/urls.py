from django.urls import include, path
from . import views
from accounts.api.views import router as accounts_router


urlpatterns = [
    path('optain_pair_tokens/', views.TokenObtainPairView.as_view(),
         name="optain_pair_tokens"),
    path('accounts/', include(accounts_router.urls)),
]
# api/v1/accounts/access_token/
# api/v1/accounts/refresh_token/
# api/v1/accounts/optain_pair_tokens/
# api/v1/accounts/accounts/
