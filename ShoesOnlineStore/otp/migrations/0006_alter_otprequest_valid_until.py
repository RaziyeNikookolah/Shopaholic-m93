# Generated by Django 4.2.3 on 2023-08-16 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0005_alter_otprequest_valid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 16, 14, 17, 10, 125280, tzinfo=datetime.timezone.utc)),
        ),
    ]
