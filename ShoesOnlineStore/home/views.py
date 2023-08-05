from django.shortcuts import render
from django.views import View
from shoes.models import Product


class HomeView(View):
    def get(self, request):

        return render(
            request,
            "index.html",
        )


class AboutView(View):
    def get(self, request):
        return render(request, "about.html"
                      )


class ShopView(View):
    def get(self, request):
        return render(request, "shop.html"
                      )


class CartView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "cart.html", {"product": product}
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
    def get(self, request, pk):
        product = Product.objects.filter(id=pk).select_related(
            'brand', 'category').prefetch_related('color', 'size').first()
        sizes = product.size.all()
        colors = product.color.all()

        return render(request, "shop_single.html", context={"product": product, 'sizes': sizes, "colors": colors}
                      )


class ThankyouView(View):
    def get(self, request):
        return render(request, "thankyou.html"
                      )
