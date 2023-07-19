from django.db import models
from core.models import BaseModel


class Product(BaseModel):
    code = models.CharField(max_length=10)
    brand = models.CharField(max_length=150)
    manufacturing_country = models.CharField(200)
    descriptions = models.TextField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="products")
    is_active = models.BooleanField(default=True, blank=True)
    slug = models.SlugField(max_length=250, null=True,
                            blank=True, unique=True, allow_unicode=True)

    def __str__(self) -> str:
        return "f{self.brand} {self.category}"


class ProductSize(BaseModel):
    size = models.IntegerField()
    color = models.CharField(max_length=20)
    availability_count = models.IntegerField(5)
    price = models.DecimalField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_sizes")

    def __str__(self) -> str:
        return "f{self.size}"


class ProductImage(BaseModel):
    front = models.CharField(max_length=250, null=True, blank=True)
    back = models.CharField(max_length=250, null=True, blank=True)
    left_side = models.CharField(max_length=250, null=True, blank=True)
    up = models.CharField(max_length=250, null=True, blank=True)
    right_side = models.CharField(max_length=250, null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_sizes")

    def __str__(self) -> str:
        return "image"


class Category(BaseModel):
    parent_category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="categories")
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True,
                            blank=True, unique=True, allow_unicode=True, )

    def __str__(self) -> str:
        return "f{self.title}"
