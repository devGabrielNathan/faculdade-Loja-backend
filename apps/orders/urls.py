from django.urls import path
from .views import OrderController
from .views import OrderItemController
# from .views import PurchaseController

urlpatterns = [
    path('orders/', OrderController.orders_controller),
    path('order/<uuid:pk>/', OrderController.order_controller),

    path('orderitems/', OrderItemController.order_items_controller),
    path('orderitems/<uuid:pk>/', OrderItemController.order_item_controller),

    # path('purchases/', PurchaseController.purchases_controller),
    # path('purchase/<uuid:pk>/', PurchaseController.purchase_controller),
]
