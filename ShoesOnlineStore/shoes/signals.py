from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Product, Category


@receiver(pre_save, sender=Product)
def create_product(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug_for_product(instance)


def create_unique_slug_for_product(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.brand, allow_unicode=True)

    instanceClass = instance.__class__
    qs = instanceClass.objects.filter(slug=slug)

    if qs.exists():
        new_slug = f"{slug}-{qs.first().id}"
        return create_unique_slug_for_product(instance, new_slug)
    return slug


@receiver(pre_save, sender=Category)
def create_category(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug_for_category(instance)


def create_unique_slug_for_category(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title, allow_unicode=True)

    instanceClass = instance.__class__
    qs = instanceClass.objects.filter(slug=slug)

    if qs.exists():
        new_slug = f"{slug}-{qs.first().id}"
        return create_unique_slug_for_category(instance, new_slug)
    return slug
