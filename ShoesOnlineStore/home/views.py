from django.shortcuts import render
from django.views import View
# from menu_items.models import MenuItem, Category


class HomeView(View):
    def get(self, request):
        # menu = MenuItem.objects.all()
        # categories = Category.objects.all()
        # info = RestaurantInfo.objects.first()
        return render(
            request,
            "index.html",
            # context={"menu": menu, "categories": categories, "info": info},
        )


class AboutView(View):
    def get(self, request):
        # info = RestaurantInfo.objects.first()
        return render(request, "about_page.html"
                      #   , context={"info": info}
                      )
