from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.html import format_html

from . import models


admin.site.register(models.Size)
admin.site.register(models.Color)


class CategoryAdminForm(ModelForm):
    class Meta:
        model = models.Category
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        parent_category = cleaned_data.get("parent_category")
        if self.instance.pk and parent_category and parent_category.pk == self.instance.pk:
            raise ValidationError("A category cannot be its own parent.")
        return cleaned_data


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "parent_category")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("parent_category",)
    raw_id_fields = ("parent_category",)
    search_fields = ("title",)
    form = CategoryAdminForm


class GalleryInline(admin.StackedInline):
    model = models.Gallery


class PriceInline(admin.TabularInline):
    model = models.Price


class QuantityInline(admin.TabularInline):
    model = models.Quantity


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "image_preview",
        "id",
        "brand",
        "code",
        "title",
        "descriptions",
        "category",
        "available_quantity",
        "is_active",
        "slug",
    )
    search_fields = ("code",)
    list_filter = ("modify_timestamp",)
    list_per_page = 10
    inlines = (QuantityInline, PriceInline, GalleryInline, )
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("category",)
    raw_id_fields = ("category",)
    autocomplete_fields = ("category",)  # Add autocomplete_fields for category

    def image_preview(self, obj):
        return format_html(
            '<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(
                obj.image.url
            )
        )

    image_preview.short_description = "Image Preview"


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("title",)


admin.site.register(models.Category, CategoryAdmin)
