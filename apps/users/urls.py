# urls.py
from django.urls import path
from .views import UserController

urlpatterns = [
    # Cookies para usuários não cadastrados
    path('profile/', UserController.user_profile_controller),
    path('login/', UserController.login_controller),
    path('logout/', UserController.logout_controller),
    path('register/', UserController.register_controller),
]
