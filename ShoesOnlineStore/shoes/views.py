from django.views.generic.list import ListView
from django.db.models import Q
from .models import Product, Image
from .serializer import ProductsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# IsAuthenticatedOrReadOnly permission just can run safe method for unauthenticated user
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ListCreateProductView(ListAPIView):
    queryset = Product.objects.filter(available_quantity__gte=1)
    serializer_class = ProductsSerializer
    # permission_classes = ((IsAuthenticatedOrReadOnly,))

    def get_queryset(self):
        return super().get_queryset().select_related('brand', 'category').prefetch_related('color', 'size')


class ProductUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = ((IsAuthenticatedOrReadOnly,))


class ProductSearchListView(APIView):

    def get(self, request):
        queryset = None
        if not 'search' in request.GET:
            queryset = Product.objects.filter(available_quantity__gte=1).select_related(
                'brand', 'category').prefetch_related('color', 'size')
        else:
            queryset = Product.objects.filter(brand__title__icontains=request.GET.get('search'), available_quantity__gte=1).select_related(
                'brand', 'category').prefetch_related('color', 'size')
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer_class = ProductsSerializer
    queryset = Product.objects.filter(available_quantity__gte=1)

    # def get_queryset(self, **kwargs):
    #     print(222222222222)
    #     search = self.request.GET.get('search')
    #     if search:
    #         self.request.session['search'] = search
    #     else:
    #         try:
    #             search = self.request.session['search']
    #         except:
    #             search = ''

    #     return Product.objects.all().select_related('brand', 'category').prefetch_related('color', 'size').filter(Q(title__contains=search) | Q(descriptions__contains=search))


class ProductList(APIView):
    def get(self, request):
        queryset = None
        if not 'search' in request.GET:
            queryset = Product.objects.filter(available_quantity__gte=1).select_related(
                'brand', 'category').prefetch_related('color', 'size')
        else:
            queryset = Product.objects.filter(brand__title__icontains=request.GET.get('search'), available_quantity__gte=1).select_related(
                'brand', 'category').prefetch_related('color', 'size')
        serializer = ProductsSerializer(
            queryset, many=True)  # price in special model
        return Response(serializer.data, status=status.HTTP_200_OK)
