# Generated by Django 5.0.6 on 2024-06-21 11:24

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('atualization', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='orders.order')),
                ('product_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='products.product')),
            ],
            options={
                'verbose_name': 'OrderItem',
                'verbose_name_plural': 'OrderItems',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_item',
            field=models.ManyToManyField(blank=True, related_name='order', through='orders.OrderItem', to='products.product'),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('payment_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('PENDING', 'pending'), ('CANCELED', 'cancelled'), ('COMPLETED', 'completed')], default='', max_length=255)),
                ('payment', models.CharField(choices=[('CREDIT CARD', 'credit card'), ('PIX', 'pix')], default='', max_length=255)),
                ('purchase_at', models.DateTimeField(auto_now_add=True)),
                ('atualization', models.DateTimeField(auto_now=True)),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Purchase',
                'verbose_name_plural': 'Purchases',
            },
        ),
    ]
