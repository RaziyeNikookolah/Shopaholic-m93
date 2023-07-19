from django.db import models
from core.models import BaseModel


class Order(BaseModel):
    class SendingType(models.IntegerChoices):
        TIPAX = 1, "��🚀 تیپاکس "
        POST = 2, "🚚 پست  "
        EXPRESS = 3, "🚖 تحویل در شهر"

    class DeliveryStatus(models.IntegerChoices):
        CANCLE = 0, "لغو شده ❌"
        IN_STORE = 1, "در انبار🚂"
        SENT = 2, "ارسال شده 🚛"
        RECEIVED = 3, "تحویل داده شده ✔"

    customer = models.ForeignKey(
        "Customer", on_delete=models.PROTECT, related_name="orders"
    )
    future_send_date = models.DateTimeField()
    sending_type = models.IntegerField(
        choices=SendingType.choices, default=2)
    delivery_status = models.DateTimeField()
    sending_type = models.IntegerField(
        choices=DeliveryStatus.choices, default=1)
    tracking_code = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self) -> str:
        return f"{self.delivery_status}"
