# Generated by Django 4.2.3 on 2023-07-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(0, 'User'), (1, 'Customer'), (2, 'Manager'), (3, 'Staff')], default=0, verbose_name='role'),
        ),
    ]
