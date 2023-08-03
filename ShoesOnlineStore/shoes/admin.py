from django.contrib import admin
from . import models
from django.utils.html import format_html

admin.site.register(models.Size)
admin.site.register(models.Image)
admin.site.register(models.Color)
admin.site.register(models.Category)
admin.site.register(models.Brand)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("image_preview", "id", "brand", 'code', 'price', 'descriptions',
                    'category',  'available_quantity',  'is_active', 'slug')
    search_fields = ("code", "color")
    list_filter = ("updated_at",)
    list_per_page = 10

    def image_preview(self, obj):
        return format_html(
            '<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(
                obj.image.url
            )
        )

    image_preview.short_description = "Image Preview"
