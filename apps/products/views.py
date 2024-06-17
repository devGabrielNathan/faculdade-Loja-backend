from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response


# Lista de Produtos
@api_view(['GET'])
def api_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

# Produto Único
@api_view()
def api_product(request, pk):
    product = get_object_or_404(Product, product_uuid=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
