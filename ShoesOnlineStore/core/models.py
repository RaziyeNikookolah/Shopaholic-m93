from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        abstract = True
        ordering = ("-updated_at", "-created_at")
# soft delete
# class SoftDelete()
