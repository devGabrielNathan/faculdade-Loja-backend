from rest_framework.decorators import api_view
from rest_framework.response import Response
from .repositories import OrderDao
# from .repositories import PurchaseDao
from .repositories import OrderItemDao
from .serializers import OrderSerializer
# from .serializers import PurchaseSerializer
from .serializers import OrderItemSerializer


class OrderController:
    @api_view(['GET', 'POST'])
    def orders_controller(request):
        if request.method == 'GET':
            orders = OrderDao.get_all(json=True)
            return Response(orders)
        
        elif request.method == 'POST':
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_fk=request.user)
                return Response(serializer.data, status=201)
            
            return Response(serializer.errors, status=400)


    @api_view(['GET', 'PUT', 'DELETE'])
    def order_controller(request, pk):
        order = OrderDao.get_order_by_id(pk)
        if not order:
            return Response({"error": "Order not found"}, status=404)

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
            OrderDao.delete_order(pk)
            return Response(status=204)
    

class OrderItemController:
    @api_view(['GET', 'POST'])
    def order_items_controller(request):
        if request.method == 'GET':
            order_items = OrderItemDao.get_all(json=True)
            return Response(order_items)
        
        elif request.method == 'POST':
            serializer = OrderItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            
            return Response(serializer.errors, status=400)


    @api_view(['GET', 'PUT', 'DELETE'])
    def order_item_controller(request, pk):
        order_item = OrderItemDao.get_order_item_by_id(pk)
        if not order_item:
            return Response({"error": "Order item not found"}, status=404)

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
            OrderItemDao.delete_order_item(pk)
            return Response(status=204)
    

# class PurchaseController:
#     @api_view(['GET', 'POST'])
#     def purchases_controller(request):
#         if request.method == 'GET':
#             purchases = PurchaseDao.get_all(json=True)
#             return Response(purchases)
        
#         elif request.method == 'POST':
#             serializer = PurchaseSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save(user_fk=request.user)
#                 return Response(serializer.data, status=201)
            
#             return Response(serializer.errors, status=400)


#     @api_view(['GET', 'PUT', 'DELETE'])
#     def purchase_controller(request, pk):
#         purchase = PurchaseDao.get_purchase_by_id(pk)
#         if not purchase:
#             return Response({"error": "Purchase not found"}, status=404)

#         if request.method == 'GET':
#             serializer = PurchaseSerializer(purchase)
#             return Response(serializer.data)
        
#         elif request.method == 'PUT':
#             serializer = PurchaseSerializer(purchase, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
            
#             return Response(serializer.errors, status=400)
        
#         elif request.method == 'DELETE':
#             PurchaseDao.delete_purchase(pk)
#             return Response(status=204)
