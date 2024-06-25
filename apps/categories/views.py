from rest_framework.decorators import api_view
from rest_framework.response import Response
from .repositories import CategoryDao
from .repositories import SubCategoryDao


class CategoryController:
    @api_view(['GET'])
    def categories(request):
        return Response(CategoryDao.get_all_categories(json=True))


    @api_view(['GET'])
    def category(request, pk):
        return Response(CategoryDao.get_category_by_id(pk, json=True))


class SubcategoryController:
    @api_view(['GET'])
    def subcategories(request):
        return Response(SubCategoryDao.get_all_subcategories(json=True))


    @api_view(['GET'])
    def subcategory(request, pk):
        return Response(SubCategoryDao.get_subcategory_by_id(pk, json=True))

