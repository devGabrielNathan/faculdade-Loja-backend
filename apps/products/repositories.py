from .models import Product
from .serializers import ProductSerializer
from rest_framework.exceptions import NotFound


class ProductDao:
    @staticmethod
    def get_all_products(json=False):
        products = Product.objects.all()
        if (json):
            serializer = ProductSerializer(products, many=True)
            return serializer.data
        
        else:
            return products

    # TODO: Verificar
    @staticmethod
    def get_product_by_id(pk, json=False):
        product = Product.objects.filter(product_uuid=pk).first()
        
        if not product:
            raise NotFound(detail="Product not found")
        
        if (json):
            serializer = ProductSerializer(product)
            return serializer.data
        
        else:
            return product
