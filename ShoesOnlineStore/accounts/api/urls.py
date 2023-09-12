from django.urls import path
from . import views
from accounts.api.views import router as accounts_router


urlpatterns = [
    path('optain_pair_tokens/', views.TokenObtainPairView.as_view(),
         name="optain_pair_tokens"),
    path('get_user_id_from_token/', views.get_user_id_in_token.as_view(),
         name="get_user_id_from_token")

]

# api/v1/accounts/optain_pair_tokens/
