from django.urls import path
from .views import ProductController


urlpatterns = [
    path('products/', ProductController.products),
    path('product/<uuid:pk>/', ProductController.product),
]
