from rest_framework import serializers
from .models import Order
from .models import OrderItem


class OrderSerializer(serializers.ModelSerializer):
    model = Order
    fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    model = OrderItem
    fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    model = OrderItem
    fields = '__all__'