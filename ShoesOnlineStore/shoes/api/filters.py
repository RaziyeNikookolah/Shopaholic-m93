from django_filters import rest_framework as filters
from ..models import Product, Price


class ProductFilter(filters.FilterSet):
    title = filters.CharFilter(
        field_name='title', lookup_expr='icontains', label='Search')
    category__title = filters.CharFilter(
        field_name='category__title', lookup_expr='icontains', label='Category name')
    brand__title = filters.CharFilter(
        field_name='brand__title', lookup_expr='icontains', label='Brand name')
    color__name = filters.CharFilter(
        field_name='color__name', lookup_expr='icontains', label='Color name')
    size__name = filters.CharFilter(
        field_name='size__name', lookup_expr='icontains', label='Size name')
    min_price = filters.NumberFilter(
        method='filter_min_price', label="Min price")
    max_price = filters.NumberFilter(
        method='filter_max_price', label='Max price')

    class Meta:
        model = Product
        fields = ['title', 'category__title',
                  'brand__title', 'color__name', 'size__name', 'min_price', 'max_price']

        def filter_min_price(self, queryset, name, value):
            min_price_qs = Price.objects.filter(
                price__gte=value).values_list('product', flat=True)
            queryset = queryset.filter(
                products__id__in=min_price_qs).distinct()
            return queryset

        def filter_max_price(self, queryset, name, value):
            max_price_qs = Price.objects.filter(
                price__lte=value).values_list('product', flat=True)
            queryset = queryset.filter(
                products__id__in=max_price_qs).distinct()
            return queryset
