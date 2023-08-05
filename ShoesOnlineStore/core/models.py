from django.db import models
from .manager import SoftDeleteManager
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        abstract = True
        # ordering = ("-updated_at", "-created_at")
# soft delete
# class SoftDelete()


class SoftDeleteModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(
        null=True, default=None, blank=True, db_index=True)
    objects = models.Manager()
    undeleted_objects = SoftDeleteManager()
    # deleted_objects =

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True
