from django.db import models
from apps.categories.models import SubCategory
from uuid import uuid4


class Product(models.Model):
    STOCK_CHOICES = (
        ('IN_STOCK', 'in_stock'),
        ('OUT_OF_STOCK', 'out_of_stock')
    )
    product_uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default=''
    )
    brand = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    description = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default=''
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        default=0.00
    )
    image = models.ImageField(
        upload_to='products/images/',
        blank=False,
        null=False
    )
    status = models.CharField(
        max_length=255,
        choices=STOCK_CHOICES,
        default='IN_STOCK'
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
    subcategory_fk = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name="products"
    )


    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
