# Generated by Django 4.2.3 on 2023-08-05 12:59

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
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 5, 13, 1, 51, 219137, tzinfo=datetime.timezone.utc)),
        ),
    ]
