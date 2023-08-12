# Generated by Django 4.2.3 on 2023-08-11 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shoes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('restore_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Ordered'), (2, 'New')], default=2, verbose_name='status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('restore_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='quantity')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='cart.cart', verbose_name='cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cart_items', to='shoes.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'cart item',
                'verbose_name_plural': 'cart items',
                'unique_together': {('cart', 'product')},
            },
        ),
    ]