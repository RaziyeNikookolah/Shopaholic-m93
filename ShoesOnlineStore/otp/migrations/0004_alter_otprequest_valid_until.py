# Generated by Django 4.2.3 on 2023-08-05 18:19

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
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 5, 18, 21, 18, 124268, tzinfo=datetime.timezone.utc)),
        ),
    ]
