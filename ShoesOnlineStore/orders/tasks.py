from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True)
def send_delivery_status_email(self, order_id,):
    from .models import Order
    order = Order.objects.get(id=order_id)
    target_mail = order.email
    mail_subject = 'Your order Send today'
    message = f'Order was sent successfully'
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[target_mail],
        fail_silently=False,
    )
    return f"Email sent to {target_mail} successfully"


@shared_task(bind=True)
def send_order_paid_email(self, order_id,):
    from .models import Order
    order = Order.objects.get(id=order_id)
    target_mail = 'shoes.online.shop.supervisor2023@gmail.com'
    mail_subject = 'One Order paid now'
    message = f'Order {order}'
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[target_mail],
        fail_silently=False,
    )
    return f"Email sent to {target_mail} successfully"
