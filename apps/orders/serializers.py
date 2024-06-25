from rest_framework import serializers
from .models import Order
from .models import OrderItem
# from .models import Purchase


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


# class PurchaseSerializer(serializers.ModelSerializer):
#     model = Purchase
#     fields = '__all__'