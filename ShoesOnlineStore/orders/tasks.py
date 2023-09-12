import csv
from celery import shared_task
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone
import os


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
def send_order_paid_email(self, order_id):
    from .models import Order
    order = Order.objects.get(id=order_id)
    target_mail = 'r.nikookolah@gmail.com'
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


@shared_task(bind=True)
def email_export(self):  # no one can not call this view use user_passes_test
    export_dir = 'C:\\exports'
    # Create the directory if it doesn't exist
    os.makedirs(export_dir, exist_ok=True)
    # export_dir = os.path.join(settings.BASE_DIR, 'exports')
    csv_file_path = os.path.join(export_dir, 'orders.csv')
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Products in order:'])
    today = timezone.now().date()
    from orders.models import Order, OrderItem
    orders_created_today = Order.objects.filter(create_timestamp__date=today).select_related('items').values(
        'id', 'create_timestamp', 'is_paid', 'receiver_name', 'receiver_lastname', 'city')

    for order in orders_created_today:
        writer.writerow([order['create_timestamp'], order['is_paid'],
                        order['receiver_name'], order['receiver_lastname'], order['city']])

        items = OrderItem.objects.filter(order_id=order['id'])
        for item in items:

            writer.writerow([item.product, item.quantity, item.final_price])

    response['Content-Disposition'] = 'attachment; filename="orders.csv"'
    with open(csv_file_path, 'w') as file:
        file.write(response.content.decode('utf-8'))

    mail_subject = 'Today Export'
    target_mail = 'r.nikookolah@gmail.com'
    message = f'Order was sent successfully'

    email = EmailMessage(
        subject=mail_subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[target_mail],
        reply_to=[target_mail],
    )

    email.attach_file(csv_file_path)  # Attach the generated CSV file
    email.send()

    return 'Exported orders to orders.csv and sent email with attachment'
