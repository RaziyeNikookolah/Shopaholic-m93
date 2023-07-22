# Generated by Django 4.2.3 on 2023-07-20 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='shoes.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('brand', models.CharField(max_length=150)),
                ('manufacturing_country', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descriptions', models.TextField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shoes.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('size', models.PositiveSmallIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='shoes.product')),
            ],
            options={
                'verbose_name_plural': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('front', models.ImageField(blank=True, default='', null=True, upload_to='get_upload_path')),
                ('back', models.ImageField(blank=True, default='', null=True, upload_to='get_upload_path')),
                ('left_side', models.ImageField(blank=True, default='', null=True, upload_to='get_upload_path')),
                ('up', models.ImageField(blank=True, default='', null=True, upload_to='get_upload_path')),
                ('right_side', models.ImageField(blank=True, default='', null=True, upload_to='get_upload_path')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shoes.product')),
            ],
            options={
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('color', models.CharField(max_length=20)),
                ('availability_count', models.PositiveSmallIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='shoes.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='shoes.size')),
            ],
            options={
                'verbose_name_plural': 'Colors',
            },
        ),
    ]
