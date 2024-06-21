from django.urls import path
from .views import ProductController


urlpatterns = [
    # Acessa todos os produtos
    path('products/', ProductController.products),
    # Acessa um único produto
    path('product/<uuid:pk>/', ProductController.product),
]
