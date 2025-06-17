from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Email", unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    # TODO remove blank=True option when deploy product
    username = models.CharField(max_length=255, blank=True, unique=True)

    EMAIL_FIELD = 'email'  # define el campo principal para manejar la autenticacion