from django.test import TestCase
from ..models import Product, Brand, Quantity, Size, Color, Gallery, Category, Price


class ProductModelTest(TestCase):
    def test_str_representation(self):
        brand = Brand.objects.create(title="Nike", manufacturing_country="USA")
        category = Category.objects.create(title="Footwear")
        product = Product.objects.create(
            title="Running Shoes", brand=brand, code="ABC123", category=category
        )
        self.assertEqual(str(product), f"{product.code},{product.brand}")


class BrandModelTest(TestCase):
    def test_str_representation(self):
        brand = Brand.objects.create(title="Nike", manufacturing_country="USA")
        self.assertEqual(str(brand), brand.title)


class QuantityModelTest(TestCase):
    def test_str_representation(self):
        brand = Brand.objects.create(title="Nike", manufacturing_country="USA")
        category = Category.objects.create(title="Footwear")
        product = Product.objects.create(
            title="Running Shoes", brand=brand, code="ABC123", category=category
        )
        quantity = Quantity.objects.create(product=product, quantity=100)
        self.assertEqual(str(quantity), str(quantity.quantity))


class SizeModelTest(TestCase):
    def test_str_representation(self):
        size = Size.objects.create(name=Size.SHOES_SIZE_NAME.ADULT, number=42)
        self.assertEqual(str(size), str(size.number))

# Similarly, write test cases for other models
