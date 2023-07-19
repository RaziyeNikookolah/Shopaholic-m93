from django.contrib import admin
from . import models

admin.site.register(models.Product)
admin.site.register(models.ProductSize)
admin.site.register(models.ProductImage)
admin.site.register(models.Category)
