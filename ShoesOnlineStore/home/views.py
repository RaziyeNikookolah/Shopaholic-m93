from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):

        return render(
            request,
            "index.html",
        )


class AboutView(View):
    def get(self, request):
        return render(request, "about_page.html"
                      )
