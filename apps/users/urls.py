# urls.py
from django.urls import path
from .views import UserController

urlpatterns = [
    # Cookies para usuários não cadastrados
    path('user/', UserController.user),
    path('login/', UserController.login),
    path('logout/', UserController.logout),
    path('register/', UserController.register),
]
