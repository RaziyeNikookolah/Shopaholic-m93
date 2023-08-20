# Generated by Django 4.2.3 on 2023-08-17 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='receiver_phone_number',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='city'),
        ),
    ]