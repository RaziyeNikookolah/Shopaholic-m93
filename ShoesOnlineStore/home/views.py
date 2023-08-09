from django.core import serializers
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shoes.serializer import ProductsSerializer
from django.db.models import OuterRef, Subquery
from shoes.models import Product, Price


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
    def get(self, request):
        # product = Product.objects.get(pk=pk)
        return render(request, "cart.html"  # , {"product": product}
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
        last_price_subquery = Price.objects.filter(
            product=OuterRef('pk')).order_by('-create_timestamp')

        product = Product.objects.filter(id=pk).select_related('brand', 'category').prefetch_related('color', 'size'
                                                                                                     ).annotate(
            last_price=Subquery(last_price_subquery.values('price')[:1])
        ).first()
        sizes = product.size.all()
        colors = product.color.all()
        return render(request, "shop_single.html", {"product": product, "sizes": sizes, "colors": colors})


class ThankyouView(View):
    def get(self, request):
        return render(request, "thankyou.html"
                      )


class ShoeDetail(APIView):
    def get(self, request, pk):
        last_price_subquery = Price.objects.filter(
            product=OuterRef('pk')).order_by('-create_timestamp')

        product = Product.objects.filter(id=pk).select_related('brand', 'category').prefetch_related('color', 'size'
                                                                                                     ).annotate(
            last_price=Subquery(last_price_subquery.values('price')[:1])
        ).first()
        serializer = ProductsSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
