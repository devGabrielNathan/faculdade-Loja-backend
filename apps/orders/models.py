from ..products.models import Product
from ..users.models import User
from django.db import models
from uuid import uuid4


class Order(models.Model):
    order_uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    atualization = models.DateTimeField(
        auto_now=True
    )
    active = models.BooleanField(
        default=True
    )
    order_item = models.ManyToManyField(
        Product,
        related_name='order',
        blank=True,
        through='OrderItem'
    )
    user_fk = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='order'
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


    def __str__(self) -> str:
        return self.atualization

class Purchase(models.Model):
    payment_uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    STATUS_CHOICES = {
    ('PENDING', 'pending'),
    ('COMPLETED', 'completed'),
    ('CANCELED', 'cancelled')
    }
    PAYMENT_CHOICES = (
    ('CREDIT CARD', 'credit card'),
    ('PIX', 'pix'),
    )
    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default=''
    )
    payment = models.CharField(
        max_length=255,
        choices=PAYMENT_CHOICES,
        default=''
    )
    purchase_at = models.DateTimeField(
        auto_now_add=True
    )
    atualization = models.DateTimeField(
        auto_now=True
    )
    user_fk = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='purchase'
    )


    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'


    def __str__(self) -> str:
        return self.atualization



class OrderItem(models.Model):
    order_fk = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='orderitem'
    ) 
    product_fk = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='orderitem'
    )
    quantity = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'


    def __str__(self) -> str:
        return self.quantity

