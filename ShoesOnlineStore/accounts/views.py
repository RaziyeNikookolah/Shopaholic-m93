from django.shortcuts import render

# Create your views here.
from .forms import UserCreationOrLoginForm
from django.views import View


class LoginView(View):
    template_name = "accounts/login.html"

    def get(self, request, *args, **kwargs):

        form = UserCreationOrLoginForm()
        return render(request, self.template_name, {"form": form})
