from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    username = models.CharField(
        max_length=255
    )
    email = models.CharField(
        max_length=255,
        unique=True
    )
    password = models.CharField(
        max_length=255, 
    )

    # Faz com que ao invéz de solicitar o username para login ele utilize o campo email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


