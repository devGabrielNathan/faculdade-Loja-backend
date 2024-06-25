from .models import Category
from .models import SubCategory
from .serializers import CategorySerializer
from .serializers import SubCategorySerializer
from rest_framework.exceptions import NotFound


class CategoryDao:
    @staticmethod
    def get_all_categories(json=False):
        categories = Category.objects.all()
        if json:
            serializer = CategorySerializer(categories, many=True)
            return serializer.data
        else:
            return categories

    @staticmethod
    def get_category_by_id(pk, json=False):
        category = Category.objects.filter(category_uuid=pk).first()

        if not category:
            raise NotFound(detail="Category not found")
        
        if json:
            serializer = CategorySerializer(category)
            return serializer.data
        else:
            return category

class SubCategoryDao:
    @staticmethod
    def get_all_subcategories(json=False):
        subcategories = SubCategory.objects.all()

        if json:
            serializer = SubCategorySerializer(subcategories, many=True)
            return serializer.data
        else:
            return subcategories
    
    @staticmethod
    def get_subcategory_by_id(pk, json=False):
        subcategory = SubCategory.objects.filter(subcategory_uuid=pk).first()

        if not subcategory:
            raise NotFound(detail="Subcategory not found")
        
        if json:
            serializer = SubCategorySerializer(subcategory)
            return serializer.data
        else:
            return subcategory
