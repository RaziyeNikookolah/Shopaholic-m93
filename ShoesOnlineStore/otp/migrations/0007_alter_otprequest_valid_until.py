# Generated by Django 4.2.3 on 2023-08-16 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0006_alter_otprequest_valid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 16, 21, 34, 28, 428867, tzinfo=datetime.timezone.utc)),
        ),
    ]
