from django.urls import include, path


urlpatterns = [
    path('accounts/', include("accounts.api.urls")),]
