from django.test import TestCase
from django_filters import CharFilter, NumberFilter
from model_bakery import baker
from shoes.models import Product, Price
from shoes.api.filters import ProductFilter


class ProductFilterTests(TestCase):

    def test_filter_fields(self):
        filterset = ProductFilter()
        self.assertIsInstance(filterset.filters['title'], CharFilter)
        self.assertIsInstance(filterset.filters['category__title'], CharFilter)
        self.assertIsInstance(filterset.filters['brand__title'], CharFilter)
        self.assertIsInstance(filterset.filters['color__name'], CharFilter)
        self.assertIsInstance(filterset.filters['size__name'], CharFilter)
        # self.assertIsInstance(filterset.filters['min_price'], NumberFilter)
        # self.assertIsInstance(filterset.filters['max_price'], NumberFilter)

    def test_filter_min_price(self):
        product = baker.make(Product)
        price = baker.make(Price, product=product, price=50)
        filterset = ProductFilter(
            {'min_price': 40}, queryset=Product.objects.all())
        self.assertIn(product, filterset.qs)

    def test_filter_max_price(self):
        product = baker.make(Product)
        price = baker.make(Price, product=product, price=80)
        filterset = ProductFilter(
            {'max_price': 100}, queryset=Product.objects.all())
        self.assertIn(product, filterset.qs)
