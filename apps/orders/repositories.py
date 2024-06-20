from .models import Order
from .models import Purchase
from .models import OrderItem
from .serializers import OrderSerializer
from .serializers import PurchaseSerializer
from .serializers import OrderItemSerializer 


class OrderDao:
    @staticmethod
    def get_all(json=False):
        orders = Order.objects.all()
        if (json):
            serializer = OrderSerializer(orders, many=True)
            return serializer.data
        else:
            return orders
        

class OrderItemDao:
    @staticmethod
    def get_all(json=False):
        orders_itens = OrderItem.objects.all()
        if (json):
            serializer = OrderItemSerializer(orders_itens, many=True)
            return serializer.data
        else:
            return orders_itens


class PurchaseDao:
    @staticmethod
    def get_all(json=False):
        purchase = Purchase.objects.all()
        if (json):
            serializer = PurchaseSerializer(purchase, many=True)
            return serializer.data     
        else:
            return purchase





# class OrderDAO:
#   def obterTodos(self, json=False):
#     orders = Order.Model.....
#     if(json):
#        s = Serializer...
#        return s.data
#     else
#        return orders