from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from django.contrib.auth import logout
from rest_framework.views import APIView
from core.utils import PROVINCES

# View for rendering the login page


class LoginView(View):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        # TODO: Handle form logic if needed
        return render(request, self.template_name)

# View for rendering the logout page


class LogoutView(View):
    template_name = "logout.html"

    def get(self, request, *args, **kwargs):
        # TODO: Handle form logic if needed
        return render(request, self.template_name)

# API view for handling user logout requests


class RequestLogoutView(APIView):
    def get(self, request, *args, **kwargs):
        # Log out the user
        logout(request)
        return Response({"message": "logout successfully"}, status=status.HTTP_200_OK)


class ProfileView(APIView):
    template_name = "profile.html"

    def get(self, request, *args, **kwargs):
        # TODO: Handle form logic if needed
        return render(request, self.template_name, {"PROVINCES": PROVINCES})
