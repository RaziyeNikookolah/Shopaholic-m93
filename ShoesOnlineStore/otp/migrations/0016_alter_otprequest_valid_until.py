# Generated by Django 4.2.3 on 2023-08-26 11:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0015_otprequest_create_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 26, 12, 0, 29, 246360, tzinfo=datetime.timezone.utc)),
        ),
    ]
