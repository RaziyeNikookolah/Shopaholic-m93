from django.db import models
from core.models import BaseModel


class Product(BaseModel):
    class Meta:
        verbose_name_plural = "Products"
    code = models.CharField(max_length=10)
    brand = models.CharField(max_length=150)
    manufacturing_country = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    descriptions = models.TextField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="products")
    is_active = models.BooleanField(default=True, blank=True)
    slug = models.SlugField(max_length=250, null=True,
                            blank=True, unique=True, allow_unicode=True)

    def __str__(self) -> str:
        return f"{self.brand} {self.category}"


class Size(BaseModel):
    class Meta:
        verbose_name_plural = "sizes"
    size = models.PositiveSmallIntegerField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="sizes")

    def __str__(self) -> str:
        return f"{self.size}"


class Color(BaseModel):
    class Meta:
        verbose_name_plural = "Colors"
    color = models.CharField(max_length=20)
    availability_count = models.PositiveSmallIntegerField()
    size = models.ForeignKey(
        Size, on_delete=models.CASCADE, related_name="colors")

    def __str__(self) -> str:
        return f"{self.color}"


class Image(BaseModel):
    class Meta:
        verbose_name_plural = "Images"

    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="images")
    front = models.ImageField(
        upload_to='get_upload_path', default="", null=True, blank=True)

    back = models.ImageField(
        upload_to='get_upload_path', default="", null=True, blank=True)

    left_side = models.ImageField(
        upload_to='get_upload_path', default="", null=True, blank=True)

    up = models.ImageField(
        upload_to='get_upload_path', default="", null=True, blank=True)

    right_side = models.ImageField(
        upload_to='get_upload_path', default="", null=True, blank=True)

    def __str__(self) -> str:
        return "image"

    @staticmethod
    def get_upload_path(instance, filename):
        # TODO filenameshould be field name
        return f"statics/shoes/images/{instance.product.id}/{filename}"


class Category(BaseModel):
    class Meta:
        verbose_name_plural = "Categories"
    parent_category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="categories", null=True,
        blank=True,
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True,
                            blank=True, unique=True, allow_unicode=True, )

    def __str__(self) -> str:
        return f"{self.title}"
