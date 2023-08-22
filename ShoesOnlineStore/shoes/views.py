from django.db.models import Subquery, OuterRef, Max
from django_filters.rest_framework import DjangoFilterBackend
from shoes.pagination import ProductPagination
from .models import Product, Price

from .serializer import ProductsSerializer
from rest_framework.permissions import AllowAny
# IsAuthenticatedOrReadOnly permission just can run safe method for unauthenticated user
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status, filters
from shoes.api.filters import ProductFilter


class ProductList(ListAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = ProductsSerializer
    queryset = Product.objects.filter(
        available_quantity__gte=1
    ).select_related('brand', 'category').prefetch_related('color', 'size')

    def get_queryset(self):

        last_price_subquery = Price.objects.filter(
            product=OuterRef('pk')).order_by('-create_timestamp')
        last_price_subquery = last_price_subquery.values('price')[:1]

        queryset = super().get_queryset().annotate(
            last_price=Subquery(last_price_subquery)
        )
        return queryset
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filterset_fields = ["title", "category__title", "brand__title"]
    filter_class = ProductFilter
    search_fields = [
        'title',
        'brand__title',
        'brand__manufacturing_country',
        'descriptions',
        'size__number',
        'color__name',]

