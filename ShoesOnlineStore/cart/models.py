from shoes.models import Product
from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Cart(BaseModel):
    class Status(models.IntegerChoices):

        ORDERED = 1, _('Ordered')
        NEW = 2, _('New')

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('user'), related_name='carts')
    status = models.IntegerField(
        _('status'), choices=Status.choices, default=Status.NEW)

    class Meta:
        verbose_name = _("cart")
        verbose_name_plural = _('carts')

    def __str__(self) -> str:
        return f'{self.user}: {self.status}'


class CartItem(BaseModel):

    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, verbose_name=_('cart'), related_name='cart_items')
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, verbose_name=_('product'), related_name='cart_items')
    quantity = models.PositiveIntegerField(_('quantity'))

    class Meta:
        verbose_name = _("cart item")
        verbose_name_plural = _('cart items')
        unique_together = ['cart', 'product']

    def __str__(self) -> str:
        return str(self.id)
