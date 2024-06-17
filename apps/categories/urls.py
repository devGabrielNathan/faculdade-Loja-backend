from django.urls import path
from . import views


urlpatterns = [
    # URLs para categorias
    path('', views.api_categories),
    path('category/<uuid:pk>/', views.api_category),

    # URLs para subcategorias
    path('subcategories/', views.api_subcategories),
    path('subcategory/<uuid:pk>/', views.api_subcategory),
]
