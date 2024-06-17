from .models import Category
from .models import SubCategory
from .serializers import CategorySerializer
from .serializers import SubCategorySerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


@api_view(['GET'])
def api_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_category(request, pk):
    category = get_object_or_404(Category, category_uuid=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['GET'])
def api_subcategories(request):
    subcategories = SubCategory.objects.all()
    serializer = SubCategorySerializer(subcategories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_subcategory(request, pk):
    subcategory = get_object_or_404(SubCategory, subcategories_uuid=pk)
    serializer = SubCategorySerializer(subcategory)
    return Response(serializer.data)

