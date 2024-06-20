from .models import Category
from .models import SubCategory
from .serializers import CategorySerializer
from .serializers import SubCategorySerializer


class CategoryDao:
    @staticmethod
    def get_all_categories(json=False):
        categories = Category.objects.all()
        if (json):
            serializer = CategorySerializer(categories, many=True)
            return serializer.data
        else:
            return categories

    # TODO: Verificar
    @staticmethod
    def get_category_by_id(pk, json=False):
        category = Category.objects.filter(category_uuid=pk)
        if (json):
            serializer = CategorySerializer(category)
            return serializer.data
        else:
            return category

class SubCategoryDao:
    @staticmethod
    def get_all_subcategories(json=False):
        subcategories = SubCategory.objects.all()
        if (json):
            serializer = SubCategorySerializer(subcategories, many=True)
            return serializer.data
        else:
            return subcategories
    
    # TODO: Verificar  
    def get_category_by_id(pk, json=False):
        subcategory = Category.objects.filter(subcategory_uuid=pk)
        if (json):
            serializer = CategorySerializer(subcategory)
            return serializer.data
        else:
            return subcategory
