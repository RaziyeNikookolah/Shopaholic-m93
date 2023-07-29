# Generated by Django 4.2.3 on 2023-07-29 04:57

import core.validators
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(error_messages={'unique': 'A user with that phone number already exists.'}, help_text='Required. 11 character. digits only.', max_length=14, unique=True, validators=[core.validators.PhoneValidator()], verbose_name='phone number')),
                ('role', models.PositiveSmallIntegerField(choices=[(0, 'User'), (1, 'Customer'), (2, 'Manager'), (3, 'Staff')], default=0, verbose_name='role')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='OtpRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=14)),
                ('code', models.CharField(max_length=4, null=True)),
                ('valid_until', models.DateTimeField(default=datetime.datetime(2023, 7, 29, 4, 59, 40, 619963, tzinfo=datetime.timezone.utc))),
            ],
            options={
                'verbose_name': 'OneTimePassword',
                'verbose_name_plural': 'OneTimePasswords',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], default=2, verbose_name='gender')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('image', models.ImageField(blank=True, default='statics/profile/images/profile.jpg', null=True, upload_to='statics/profile/images/', verbose_name='image')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('province', models.CharField(choices=[('thr', 'Tehran'), ('az-sh', 'Azarbayejan Sharghi'), ('az-gh', 'Azarbayejan Gharbi'), ('ard', 'Ardebil'), ('esf', 'Esfehan'), ('alb', 'Alborz'), ('ilm', 'Ilam'), ('bsh', 'Booshehr'), ('chm', 'Charmahal o Bakhtiari'), ('kh-j', 'Khorasan Jonobi'), ('kh-r', 'Khorasan Razavi'), ('kh-sh', 'Khorasan Shomali'), ('khz', 'Khoozestan'), ('znj', 'Zanjan'), ('smn', 'Semnan'), ('sbch', 'Sistan Baloochestan'), ('frs', 'Fars'), ('ghz', 'Ghazvin'), ('qom', 'Qom'), ('krd', 'Kordestan'), ('krm', 'Kerman'), ('kr-sh', 'Kerman Shah'), ('khb', 'Kohkilooye Boyer Ahmad'), ('gls', 'Golestan'), ('gil', 'Gilan'), ('lor', 'Lorestan'), ('maz', 'Mazandaran'), ('mrk', 'Markazi'), ('hrm', 'Hormozgan'), ('hmd', 'Hamedan'), ('yzd', 'Yazd')], max_length=7, verbose_name='Province')),
                ('city', models.CharField(max_length=40, verbose_name='city')),
                ('address', models.TextField(max_length=100, verbose_name='adderess')),
                ('postal_code', models.CharField(max_length=20, verbose_name='postal code')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='account')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'adresses',
            },
        ),
    ]
