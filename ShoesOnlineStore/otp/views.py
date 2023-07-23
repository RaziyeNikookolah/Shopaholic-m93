from django.shortcuts import render

from rest_framework.views import APIView


class RequestOTP(APIView):
    def post(self, request):
        ...
