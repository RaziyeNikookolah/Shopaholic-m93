from django.test import TestCase
from model_bakery import baker
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from ..models import Product, Brand, Quantity, Size, Color, Category, Price, SHOES_SIZE_NAME


class ProductModelTestCase(TestCase):

    def test_product_creation(self):
        brand = baker.make(Brand)
        category = baker.make(Category)
        color = baker.make(Color)
        size = baker.make(Size)

        product = Product.objects.create(
            title="Test Product",
            brand=brand,
            code="TP123",
            descriptions="Test description",
            available_quantity=10,
            category=category,
            image="test_image.jpg",
            is_active=True,
            slug="test-product",
        )

        product.color.add(color)
        product.size.add(size)

        self.assertEqual(str(product), f"{product.code},{product.brand}")

    def test_product_unique_code(self):
        brand = baker.make(Brand)
        category = baker.make(Category)

        Product.objects.create(
            title="Product 1",
            brand=brand,
            code="P123",
            category=category,
        )

        with self.assertRaises(IntegrityError):
            Product.objects.create(
                title="Product 2",
                brand=brand,
                code="P123",
                category=category,
            )


class QuantityModelTestCase(TestCase):

    def test_quantity_creation(self):
        product = baker.make(Product)
        quantity = Quantity.objects.create(product=product, quantity=100)
        self.assertEqual(str(quantity), str(quantity.quantity))


class SizeModelTestCase(TestCase):

    def test_size_creation(self):
        size = Size.objects.create(
            name=SHOES_SIZE_NAME.ADULT, number=40)
        self.assertEqual(str(size), str(size.number))


class ColorModelTestCase(TestCase):

    def test_color_creation(self):
        color = Color.objects.create(name="Red")
        self.assertEqual(str(color), color.name)


class CategoryModelTestCase(TestCase):

    def test_category_creation(self):
        parent_category = baker.make(Category)
        category = Category.objects.create(
            parent_category=parent_category, title="Subcategory"
        )
        self.assertEqual(str(category), category.title)


class PriceModelTestCase(TestCase):

    def test_price_creation(self):
        product = baker.make(Product)
        price = Price.objects.create(product=product, price=99.99)
        self.assertEqual(str(price), f'{price.create_timestamp}:{price.price}')
