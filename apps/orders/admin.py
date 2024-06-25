from django.contrib import admin
from .models import Order
# from .models import Purchase
from .models import OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model = Order
        fields = '__all__'


# @admin.register(Purchase)
# class PurchaseAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Purchase
#         fields = '__all__'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    class Meta:
        model = OrderItem
        fields = '__all__'
