# Generated by Django 4.2.3 on 2023-08-11 01:24

from django.db import migrations, models
import django.db.models.deletion
import shoes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('restore_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('title', models.CharField(max_length=150)),
                ('manufacturing_country', models.CharField(max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('restore_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='shoes.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('restore_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('restore_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('descriptions', models.TextField(blank=True, max_length=250, null=True)),
                ('available_quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='shoe_images/')),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shoes.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shoes.category')),
                ('color', models.ManyToManyField(related_name='products', to='shoes.color')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('restore_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('number', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('restore_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quantities', to='shoes.product', verbose_name='product')),
            ],
            options={
                'verbose_name_plural': 'Quantities',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(related_name='products', to='shoes.size'),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('restore_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='price')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='shoes.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'price',
                'verbose_name_plural': 'prices',
                'ordering': ('-create_timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('restore_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('front', models.ImageField(blank=True, default='', null=True, upload_to=shoes.models.Gallery.get_upload_path)),
                ('back', models.ImageField(blank=True, default='', null=True, upload_to=shoes.models.Gallery.get_upload_path)),
                ('left_side', models.ImageField(blank=True, default='', null=True, upload_to=shoes.models.Gallery.get_upload_path)),
                ('up', models.ImageField(blank=True, default='', null=True, upload_to=shoes.models.Gallery.get_upload_path)),
                ('right_side', models.ImageField(blank=True, default='', null=True, upload_to=shoes.models.Gallery.get_upload_path)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='shoes.product')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
    ]
