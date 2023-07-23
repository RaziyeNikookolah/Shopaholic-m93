from django.contrib import admin
from . import models

admin.site.register(models.Account)
admin.site.register(models.Profile)
admin.site.register(models.Address)
admin.site.register(models.OtpRequest)
