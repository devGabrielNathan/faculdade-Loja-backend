from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .serializers import OrderSerializer
from .serializers import OrderItemSerializer
from .serializers import PurchaseSerializer
from .models import Order
from .models import Purchase
from .models import OrderItem
from rest_framework.response import Response
from .repositories import OrderDao
from .repositories import OrderItem
from .repositories import PurchaseDao


class Order:
    # Faz a solicitação de todas as orders do banco de dados
    @staticmethod
    @api_view(['GET', 'POST'])
    def orders_controller(request):
        if request.method == 'GET':
            return Response(OrderDao.get_all(json=True))
        
        elif request.method == 'POST':
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_fk=request.user)
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)


    # Faz a solicitação de apenas uma orde do banco de dados
    @staticmethod
    @api_view(['GET', 'PUT', 'DELETE'])
    def order_controller(request, pk):
        order = get_object_or_404(Order, order_uuid=pk)
        if request.method == 'GET':
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = OrderSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            
            return Response(serializer.errors, status=400)
        
        elif request.method == 'DELETE':
            order.delete()
            return Response(status=204)


class OrderItem:
    # Faz a solicitação de um  as ordersitems do banco de dados
    @staticmethod
    @api_view(['GET', 'POST'])
    def orders_items_controller(request):
        if request.method == 'GET':
            order_items = OrderItem.objects.all()
            serializer = OrderItemSerializer(order_items, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = OrderItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        

    @staticmethod
    @api_view(['GET', 'PUT', 'DELETE'])
    def order_item_controller(request, pk):
        order_item = get_object_or_404(OrderItem, id=pk)
        if request.method == 'GET':
            serializer = OrderItemSerializer(order_item)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = OrderItemSerializer(order_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        elif request.method == 'DELETE':
            order_item.delete()
            return Response(status=204)


class Purchase:
    @staticmethod
    @api_view(['GET', 'POST'])
    def purchases_controller(request):
        if request.method == 'GET':
            purchases = Purchase.objects.all()
            serializer = PurchaseSerializer(purchases, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = PurchaseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_fk=request.user)
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        
        
    @staticmethod
    @api_view(['GET', 'PUT', 'DELETE'])
    def purchase_controller(request, pk):
        purchase = get_object_or_404(Purchase, payment_uuid=pk)
        if request.method == 'GET':
            serializer = PurchaseSerializer(purchase)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = PurchaseSerializer(purchase, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        elif request.method == 'DELETE':
            purchase.delete()
            return Response(status=204)
