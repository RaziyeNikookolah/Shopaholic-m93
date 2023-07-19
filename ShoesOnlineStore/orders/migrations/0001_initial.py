# Generated by Django 4.2.3 on 2023-07-19 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shoes', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sending_type', models.IntegerField(choices=[(1, '🚀🛰🚀🛰🚀 تیپاکس '), (2, '🚚 پست  '), (3, '🚖 تحویل در شهر')], default=2)),
                ('delivery_status', models.IntegerField(choices=[(0, 'لغو شده ❌'), (1, 'در انبار🚂'), (2, 'ارسال شده 🚛'), (3, 'تحویل داده شده ✔')], default=1)),
                ('tracking_code', models.CharField(blank=True, max_length=30, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='customers.customer')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receipts', to='orders.order')),
            ],
            options={
                'verbose_name_plural': 'Receipts',
            },
        ),
        migrations.CreateModel(
            name='Order_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_products', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_products', to='shoes.product')),
            ],
            options={
                'verbose_name_plural': 'Order-products',
            },
        ),
    ]
