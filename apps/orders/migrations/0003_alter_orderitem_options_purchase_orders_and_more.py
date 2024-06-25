# Generated by Django 5.0.6 on 2024-06-25 01:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={},
        ),
        migrations.AddField(
            model_name='purchase',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='purchases', to='orders.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='orders.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='products.product'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='payment',
            field=models.CharField(choices=[('CREDIT CARD', 'credit card'), ('PIX', 'pix')], default='CREDIT CARD', max_length=255),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('PENDING', 'pending'), ('CANCELED', 'cancelled'), ('COMPLETED', 'completed')], default='PENDING', max_length=255),
        ),
    ]