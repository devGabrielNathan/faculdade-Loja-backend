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


    # def calculate_total(self):
    #     total = 0
    #     for item in self.orderitems.all():
    #         total += item.get_subtotal()
    #     return total
    

    def __str__(self) -> str:
        return f"{self.user_fk.name}"
    

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    order_fk = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='orderitems'
    )
    product_fk = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='orderitems'
    )
    quantity = models.PositiveIntegerField(
        default=1
    )


    def get_subtotal(self):
        return self.quantity * self.product_fk.price


    def __str__(self) -> str:
        subtotal = self.get_subtotal()
        return f"{self.order_fk.user_fk.name}: {self.product_fk.name} x {self.quantity} - Total: R${subtotal:.2f}"


# class Purchase(models.Model):
#     payment_uuid = models.UUIDField(
#         primary_key=True,
#         default=uuid4,
#         editable=False
#     )
#     STATUS_CHOICES = {
#         ('PENDING', 'pending'),
#         ('COMPLETED', 'completed'),
#         ('CANCELED', 'cancelled')
#     }
#     PAYMENT_CHOICES = (
#         ('CREDIT CARD', 'credit card'),
#         ('PIX', 'pix'),
#     )
#     status = models.CharField(
#         max_length=255,
#         choices=STATUS_CHOICES,
#         default='PENDING'
#     )
#     payment = models.CharField(
#         max_length=255,
#         choices=PAYMENT_CHOICES,
#         default='CREDIT CARD'
#     )
#     purchase_at = models.DateTimeField(
#         auto_now_add=True
#     )
#     atualization = models.DateTimeField(
#         auto_now=True
#     )
#     user_fk = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='purchase'
#     )
#     orders = models.ManyToManyField(
#         Order,
#         related_name='purchases',
#         blank=True
#     )


#     def calculate_total(self):
#         total = 0
#         for order in self.orders.all():
#             total += order.calculate_total()
#         return total
    

#     def __str__(self) -> str:
#         total = self.calculate_total()
#         return f"{self.payment_uuid}: R${total:.2f}"


#     class Meta:
#         verbose_name = 'Purchase'
#         verbose_name_plural = 'Purchases'