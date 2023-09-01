from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect, render
from django.shortcuts import render
from django.views import View
from django.contrib.auth import logout
from core.utils import PROVINCES


class LoginView(View):
    template_name = "login.html"

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next')

        return super().setup(request, *args, **kwargs)

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:

    #         return redirect(self.next)
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class LogoutView(View):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        # Log out the user
        logout(request)
        return render(request, self.template_name)


class ProfileView(View):

    template_name = "profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"PROVINCES": PROVINCES})
