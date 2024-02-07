from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=200, unique=True, verbose_name='Электронная почта')
    phone = models.CharField(max_length=35, verbose_name='phone number', null=True, blank=True)
    image = models.ImageField(upload_to='users/', verbose_name='image', null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name='country', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
