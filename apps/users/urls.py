# urls.py
from django.urls import path
from .views import api_register
from .views import api_login
from .views import api_logout

urlpatterns = [
    path('register/', api_register, name='register'),
    path('login/', api_login, name='login'),
    path('logout/', api_logout, name='logout'),
]
