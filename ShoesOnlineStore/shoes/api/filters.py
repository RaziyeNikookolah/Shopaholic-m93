import django_filters
from ..models import Product


class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        model = Product
        fields = {
            'title': ['icontains'],
            'brand__title': ['icontains'],
            'brand__manufacturing_country': ['icontains'],
            'descriptions': ['icontains'],
            'size': ['icontains'],
            'color__name': ['exact'],
            # 'price':['lt','gt'],
        }
