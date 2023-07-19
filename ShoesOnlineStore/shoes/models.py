from django.db import models
from core.models import BaseModel


class Product(BaseModel):
    code = models.CharField(max_length=10)
    brand = models.CharField(max_length=150)
    manufacturing_country = models.CharField(200)
    descriptions = models.TextField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products")
    is_active = models.BooleanField(default=True, blank=True)


class ProductSize(BaseModel):
    ...


class ProductImage(BaseModel):
    ...


class Category(BaseModel):
    ...
