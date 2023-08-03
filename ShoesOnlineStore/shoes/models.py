from django.db import models
from core.models import BaseModel


class Product(BaseModel):
    class Meta:
        verbose_name_plural = "Products",

    def get_upload_path(instance, filename):
        return f"media/shoes/images/{instance.id}/{filename}"
    brand = models.ForeignKey(
        'Brand', on_delete=models.PROTECT, related_name="products")
    code = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    descriptions = models.TextField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="products")
    color = models.ManyToManyField(
        'Color', related_name="product_colors")
    image = models.ImageField(
        upload_to=get_upload_path, default="", null=True, blank=True)
    # galery = models.OneToOneField(
    #     "Gallery", on_delete=models.PROTECT, related_name="product_images")
    available_quantity = models.PositiveSmallIntegerField()
    size = models.ManyToManyField("Size", related_name="product_sizes")
    is_active = models.BooleanField(default=True, blank=True)
    slug = models.SlugField(max_length=250, null=True,
                            blank=True, unique=True, allow_unicode=True)

    def __str__(self) -> str:
        return f"{self.code},{self.brand} {self.category}"


class Brand (BaseModel):
    title = models.CharField(max_length=150)
    manufacturing_country = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, null=True,
                            blank=True, unique=True, allow_unicode=True)

    class Meta:
        verbose_name_plural = "Brands"

    def __str__(self) -> str:
        return f"{self.title}"


class Size(BaseModel):
    class Meta:
        verbose_name_plural = "sizes"
    number = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.number}"


class Color(BaseModel):
    class Meta:
        verbose_name_plural = "Colors"
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.name}"


class Image(BaseModel):

    class Meta:
        verbose_name_plural = "Images"

    def get_upload_path(instance, filename):
        return f"media/shoes/images/{instance.product.id}/{filename}"

    color = models.OneToOneField(
        Color, on_delete=models.PROTECT, related_name="image")
    front = models.ImageField(
        upload_to=get_upload_path, default="", null=True, blank=True)

    back = models.ImageField(
        upload_to=get_upload_path, default="", null=True, blank=True)

    left_side = models.ImageField(
        upload_to=get_upload_path, default="", null=True, blank=True)

    up = models.ImageField(
        upload_to=get_upload_path, default="", null=True, blank=True)

    right_side = models.ImageField(
        upload_to=get_upload_path, default="", null=True, blank=True)

    def __str__(self) -> str:
        return "image"


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
