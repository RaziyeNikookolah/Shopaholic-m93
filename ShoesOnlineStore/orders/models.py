from django.db import models
from core.models import BaseModel
from shoes.models import Product
from accounts.models import Account
from core.utils import PROVINCES
from django.utils.translation import gettext_lazy as _


class Order(BaseModel):
    class Meta:
        verbose_name_plural = "Orders"

    class SendingType(models.IntegerChoices):
        TIPAX = 1, " تکس "
        POST = 2, "🚚 پست  "
        EXPRESS = 3, "🚖 تحویل در شهر"

    class DeliveryStatus(models.IntegerChoices):
        CANCLE = 0, "لغو شده ❌"
        IN_STORE = 1, "در انبار🚂"
        SENT = 2, "ارسال شده 🚛"
        RECEIVED = 3, "تحویل داده شده ✔"

    account = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name="orders"
    )
    sending_type = models.IntegerField(
        choices=SendingType.choices, default=2)
    delivery_status = models.IntegerField(
        choices=DeliveryStatus.choices, default=1)
    tracking_code = models.CharField(max_length=30, null=True, blank=True)
    shipping_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    tax = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    # megdar dehi inja shipping cost , tax khodam bayad benevisam
    self_receive = models.BooleanField(default=True)
    # agar false bud maghadire payin baz beshe
    receiver_name = models.CharField(max_length=100, null=True, blank=True)
    receiver_lastname = models.CharField(max_length=150, null=True, blank=True)
    province = models.CharField(
        max_length=7,
        choices=PROVINCES,
        verbose_name=_('Province'),
    )
    city = models.CharField(_("city"), max_length=40)
    address = models.TextField(_("adderess"), max_length=100)
    postal_code = models.CharField(_("postal code"), max_length=20)

    def __str__(self) -> str:
        return f"Order id:{self.id}"


class Order_Product(BaseModel):
    class Meta:
        verbose_name_plural = "Order-products"
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="order_products"
    )
    order = models.ForeignKey(
        "Order", on_delete=models.PROTECT, related_name="order_products"
    )
    quantity = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.product} {self.order}"


class Receipt(BaseModel):
    class Meta:
        verbose_name_plural = "Receipts"
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, related_name="receipts"
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.final_price}"
