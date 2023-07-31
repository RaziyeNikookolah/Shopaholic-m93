from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import UserCreationOrLoginForm
from django.views import View


class LoginView(View):
    template_name = "accounts/login.html"

    def get(self, request, *args, **kwargs):

        form = UserCreationOrLoginForm()
        return render(request, self.template_name, {"form": form})


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/token',
        '/token/refresh',
    ]
    return Response(routes)


def get_phon_number(request: HttpRequest):
    print(request)
    return HttpResponse("hello")
