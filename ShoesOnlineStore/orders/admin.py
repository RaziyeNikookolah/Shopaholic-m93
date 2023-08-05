from django.contrib import admin
from . import models

admin.site.register(models.Order)
admin.site.register(models.OrderItems)
admin.site.register(models.Receipt)
