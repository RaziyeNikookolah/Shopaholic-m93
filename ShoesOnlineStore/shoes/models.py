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
    slug = models.SlugField(max_length=250, null=True, blank=True)


class ProductSize(BaseModel):
    size = models.IntegerField(max_length=2)
    color = models.CharField(max_length=20)
    availability_count = models.IntegerField(5)
    price = models.DecimalField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_sizes")


class ProductImage(BaseModel):
    front = models.CharField(max_length=250, null=True, blank=True)
    back = models.CharField(max_length=250, null=True, blank=True)
    left_side = models.CharField(max_length=250, null=True, blank=True)
    up = models.CharField(max_length=250, null=True, blank=True)
    right_side = models.CharField(max_length=250, null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_sizes")


class Category(BaseModel):
    parent_category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="categories")
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True, blank=True)
