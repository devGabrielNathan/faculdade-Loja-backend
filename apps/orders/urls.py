from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.api_orders, name='api_orders'),
    path('order/<uuid:pk>/', views.api_order, name='api_order'),
    path('orderitems/', views.api_order_items, name='api_order_items'),
    path('orderitems/<uuid:pk>/', views.api_order_item, name='api_order_item'),
    path('purchases/', views.api_purchases, name='api_purchases'),
    path('purchase/<uuid:pk>/', views.api_purchase, name='api_purchase'),
]
