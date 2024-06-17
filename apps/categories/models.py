from django.db import models
from uuid import uuid4


class Category(models.Model):
    category_uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=255,
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


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self) -> str:
        return self.name

class SubCategory(models.Model):
    subcategory_uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=255
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
    category_fk = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'


    def __str__(self) -> str:
        return f'{self.category_fk} - {self.name}'
