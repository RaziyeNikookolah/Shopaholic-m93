# Generated by Django 4.2.3 on 2023-08-20 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_rename_orderitems_orderitem_alter_order_postal_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='final_price',
        ),
    ]
