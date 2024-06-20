from rest_framework.decorators import api_view
from .repositories import ProductDao
from rest_framework.response import Response


class ProductController:
    @api_view(['GET'])
    def products(request):
        return Response(ProductDao.get_all_products(json=True))


    @api_view(['GET'])
    def product(request, pk):
        return Response(ProductDao.get_product_by_id(pk, json=True))
