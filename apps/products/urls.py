from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_products),
    path('<uuid:pk>/', views.api_product),
]
