# Generated by Django 4.2.3 on 2023-08-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=20, verbose_name='price'),
        ),
    ]