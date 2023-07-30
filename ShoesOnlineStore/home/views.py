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


class ShopView(View):
    def get(self, request):
        return render(request, "shop.html"
                      )


class CartView(View):
    def get(self, request):
        return render(request, "cart.html"
                      )


class CheckoutView(View):
    def get(self, request):
        return render(request, "checkout.html"
                      )


class ContactView(View):
    def get(self, request):
        return render(request, "contact.html"
                      )


class ShopSingleView(View):
    def get(self, request):
        return render(request, "shop_single.html"
                      )


class ThankyouView(View):
    def get(self, request):
        return render(request, "thankyou.html"
                      )
