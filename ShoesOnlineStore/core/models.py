from typing import Any, Dict, Tuple
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models.query import QuerySet


class SoftDeleteManager(models.Manager):

    def get_queryset(self, *args, **kwargs) -> QuerySet:
        return super().get_queryset(*args, **kwargs).filter(is_deleted=False)


class ArchiveDeletedManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super(*args, **kwargs).get_queryset().filter(is_deleted=True)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = SoftDeleteManager()
    all_objects = models.Manager()
    deleted_objects = ArchiveDeletedManager()

    is_deleted = models.BooleanField(
        default=False, db_index=True, null=False, blank=False)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    delete_timestamp = models.DateTimeField(
        default=None, null=True, blank=True)
    modify_timestamp = models.DateTimeField(auto_now=True)
    restore_timestamp = models.DateTimeField(
        default=None, null=True, blank=True)

    def delete(self, **kwargs) -> Tuple[int, Dict[str, int]]:
        self.is_deleted = True
        self.delete_timestamp = timezone.now()
        self.save(using=kwargs.get("using"))

    def restore(self):
        self.is_deleted = False
        self.restore_timestamp = timezone.now()
        self.save()
