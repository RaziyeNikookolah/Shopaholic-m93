from django.urls import path
from . import views
from accounts.api.views import router as accounts_router


urlpatterns = [
    path('optain_pair_tokens/', views.TokenObtainPairView.as_view(),
         name="optain_pair_tokens"),

]

# api/v1/accounts/optain_pair_tokens/
