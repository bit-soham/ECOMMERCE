# Generated by Django 5.0.1 on 2024-01-28 05:09

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_email_verified', models.BooleanField(default=False)),
                ('cash', models.DecimalField(decimal_places=2, default=1000, max_digits=10)),
                ('profile_pic', models.ImageField(default='profile_pics/default_image.png', upload_to='profile_pics/')),
                ('buyer', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('notification_type', models.CharField(choices=[('BS', 'bid_placed'), ('OB', 'outbidded'), ('D', 'default'), ('DEL', 'delivered'), ('OP', 'order_placed'), ('DS', 'delivered_status'), ('AIW', 'auction_item_won'), ('AIL', 'auction_item_lost')], default='D', max_length=3)),
                ('notification_data', models.CharField(default=None, max_length=100)),
                ('seen', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='item_images/')),
                ('description', models.TextField()),
                ('starting_bid', models.DecimalField(decimal_places=2, max_digits=8)),
                ('max_bid', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('current_bid', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('Sold', models.BooleanField(default=False)),
                ('last_bidding_datetime', models.DateTimeField(blank=True, default=None, null=True)),
                ('current_bid_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='current_buyer', to=settings.AUTH_USER_MODEL)),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('CC', 'Credit Card'), ('DC', 'Debit Card'), ('PP', 'PayPal'), ('NB', 'NetBanking'), ('UPI', 'UPI/ Google Pay/ Phone pe/ Paytm'), ('COD', 'Cash on Delivery')], default='CC', max_length=3)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('in progress', 'In Progress'), ('completed', 'Completed'), ('processing', 'Processing'), ('cancelled', 'Cancelled')], default='pending', max_length=40)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auctions.products')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('OrderID', models.BigAutoField(primary_key=True, serialize=False)),
                ('OrderDate', models.DateTimeField(auto_now_add=True)),
                ('OrderPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(300)])),
                ('TotalAmount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('buyerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('OrderItemID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auctions.products')),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('bid_id', models.IntegerField(primary_key=True, serialize=False)),
                ('bid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bid_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.products')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.ManyToManyField(blank=True, default=None, related_name='cart_items', to='auctions.products'),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('review_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rating', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('comments', models.CharField(max_length=500)),
                ('verifed', models.BooleanField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='auctions.products')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
