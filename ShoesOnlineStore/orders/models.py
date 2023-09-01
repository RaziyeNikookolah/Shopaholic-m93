from django.db import models
from core.models import BaseModel
from shoes.models import Price, Product
from accounts.models import Account
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .tasks import send_delivery_status_email, send_order_paid_email

MAX_DIGITS = settings.MAX_DIGITS
DECIMAL_PLACES = settings.DECIMAL_PLACES


class Order(BaseModel):
    class Meta:
        verbose_name_plural = "Orders"
        ordering = ('is_paid', '-modify_timestamp')

    class SendingType(models.IntegerChoices):
        TIPAX = 1, " تیپاکس "
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
    is_paid = models.BooleanField(null=True, blank=True, default=False)
    payment_date = models.DateTimeField(null=True, blank=True)
    tracking_code = models.CharField(max_length=30, null=True, blank=True)
    shipping_cost = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES, null=True, blank=True, default=20000)
    sent_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)

    tax = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES, null=True, blank=True)

    # megdar dehi inja shipping cost , tax khodam bayad benevisam
    self_receive = models.BooleanField(default=True)
    # agar false bud maghadire payin baz beshe
    receiver_name = models.CharField(max_length=100, null=True, blank=True)
    receiver_lastname = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    province = models.CharField(max_length=70)
    receiver_phone_number = models.CharField(
        max_length=150, null=True, blank=True)
    city = models.CharField(_("city"), max_length=40, null=True, blank=True)
    address = models.TextField(_("adderess"), max_length=100)
    postal_code = models.CharField(
        _("postal code"), max_length=20, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Order id:{self.id}"

    def get_total_price(self):
        items = self.items.all()
        if items.first():
            return sum(item.get_cost() for item in items)
        else:
            return 0

    def save(self, *args, **kwargs):
        if self.delivery_status == 2:
            send_delivery_status_email(self.id)
        if self.is_paid:
            send_order_paid_email(self.id)
        super(Order, self).save(*args, **kwargs)


class OrderItem(BaseModel):
    class Meta:
        verbose_name_plural = "OrderItems"
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="items"
    )
    order = models.ForeignKey(
        "Order", on_delete=models.PROTECT, related_name="items", null=True, blank=True)
    quantity = models.PositiveSmallIntegerField()

    def get_cost(self):
        last_price_query = Price.objects.filter(product=self.product).order_by(
            '-create_timestamp').values('price')[:1]

        if last_price_query:
            last_price = last_price_query[0]['price']
            return last_price * self.quantity

    def __str__(self) -> str:
        return f"{self.product} {self.order}"


class Receipt(BaseModel):
    class Meta:
        verbose_name_plural = "Receipts"
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, related_name="receipts"
    )
    total_price = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    final_price = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    is_paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.final_price}"
