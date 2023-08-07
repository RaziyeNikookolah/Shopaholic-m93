from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from core.models import BaseModel

MAX_DIGITS = settings.MAX_DIGITS
DECIMAL_PLACES = settings.DECIMAL_PLACES


class Product(BaseModel):
    class Meta:
        verbose_name_plural = "Products"
        # unique_together = [['color', 'image']]
    title = models.CharField(max_length=200)
    brand = models.ForeignKey(
        'Brand', on_delete=models.PROTECT, related_name="products")
    code = models.CharField(max_length=10, unique=True)
    descriptions = models.TextField(max_length=250, null=True, blank=True)
    available_quantity = models.PositiveIntegerField(null=True, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="products")
    color = models.ManyToManyField(
        'Color', related_name="product_colors")
    image = models.ImageField(
        upload_to="shoe_images/", default="", null=True, blank=True)
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


class Quantity (BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_('product'),  related_name='quantities')
    quantity = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Quantities"

    def __str__(self) -> str:
        return f"{self.quantity}"


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


class Gallery(BaseModel):

    class Meta:
        verbose_name_plural = "Gallery"

    def get_upload_path(instance, filename):
        return f"shoes/images/{instance.id}/{filename}"

    product = models.OneToOneField(
        "Product", on_delete=models.PROTECT, related_name="product")
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


class Price(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_('product'),  related_name='prices')
    price = models.DecimalField(
        _('price'), max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)

    class Meta:
        verbose_name = _("price")
        verbose_name_plural = _('prices')
        ordering = ('-create_timestamp',)

    def __str__(self) -> str:
        return f'{self.create_timestamp}:{self.price}'
