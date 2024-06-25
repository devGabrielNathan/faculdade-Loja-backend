from .models import Order
# from .models import Purchase
from .models import OrderItem
from .serializers import OrderSerializer
# from .serializers import PurchaseSerializer
from .serializers import OrderItemSerializer 


class OrderDao:
    @staticmethod
    def get_all(json=False):
        orders = Order.objects.all()
        if json:
            serializer = OrderSerializer(orders, many=True)
            return serializer.data
        
        return orders


    @staticmethod
    def get_order_by_id(pk):
        return Order.objects.filter(order_uuid=pk).first()


    @staticmethod
    def delete_order(pk):
        order = Order.objects.filter(order_uuid=pk).first()
        if order:
            order.delete()


class OrderItemDao:
    @staticmethod
    def get_all(json=False):
        order_items = OrderItem.objects.all()
        if json:
            serializer = OrderItemSerializer(order_items, many=True)
            return serializer.data
        
        return order_items


    @staticmethod
    def get_order_item_by_id(pk):
        return OrderItem.objects.filter(id=pk).first()


    @staticmethod
    def delete_order_item(pk):
        order_item = OrderItem.objects.filter(id=pk).first()
        if order_item:
            order_item.delete()


# class PurchaseDao:
#     @staticmethod
#     def get_all(json=False):
#         purchases = Purchase.objects.all()
#         if json:
#             serializer = PurchaseSerializer(purchases, many=True)
#             return serializer.data
        
#         return purchases


#     @staticmethod
#     def get_purchase_by_id(pk):
#         return Purchase.objects.filter(payment_uuid=pk).first()


#     @staticmethod
#     def delete_purchase(pk):
#         purchase = Purchase.objects.filter(payment_uuid=pk).first()
#         if purchase:
#             purchase.delete()
