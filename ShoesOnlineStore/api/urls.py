from django.urls import include, path
from shoes.api.views import router as shoes_router


urlpatterns = [
    path('accounts/', include("accounts.api.urls")),
    path('shoes/', include(shoes_router.urls)),

]
