# Generated by Django 4.2.3 on 2023-08-05 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtpRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=14)),
                ('code', models.CharField(max_length=4, null=True)),
                ('valid_until', models.DateTimeField(default=datetime.datetime(2023, 8, 5, 13, 1, 35, 589137, tzinfo=datetime.timezone.utc))),
            ],
            options={
                'verbose_name': 'OneTimePassword',
                'verbose_name_plural': 'OneTimePasswords',
            },
        ),
    ]
