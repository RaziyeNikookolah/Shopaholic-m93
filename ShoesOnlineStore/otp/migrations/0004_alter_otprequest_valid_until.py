# Generated by Django 4.2.3 on 2023-08-08 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0003_alter_otprequest_valid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 8, 6, 51, 8, 767350, tzinfo=datetime.timezone.utc)),
        ),
    ]
