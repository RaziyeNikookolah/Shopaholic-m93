# Generated by Django 4.2.3 on 2023-08-17 03:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0008_alter_otprequest_valid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 3, 50, 6, 53326, tzinfo=datetime.timezone.utc)),
        ),
    ]