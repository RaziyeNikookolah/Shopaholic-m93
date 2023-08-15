from django.shortcuts import render
from .forms import UserRegiterOrLoginForm
from django.views import View


class LoginView(View):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):

        # form = UserRegiterOrLoginForm()
        return render(request, self.template_name)
