from django.urls import path
from .views import CategoryController
from .views import SubcategoryController


urlpatterns = [
    # URLs para categorias
    path('categories/', CategoryController.categories),
    path('category/<uuid:pk>/', CategoryController.category),

    # URLs para subcategorias
    path('subcategories/', SubcategoryController.subcategories),
    path('subcategory/<uuid:pk>/', SubcategoryController.subcategory),
]
