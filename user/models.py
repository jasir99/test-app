import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=100, unique=True)
    phone_number = models.CharField(verbose_name='phone number', max_length=50, unique=True)
    address1 = models.CharField(verbose_name='address 1', max_length=100)
    address2 = models.CharField(verbose_name='address 2', max_length=100, null=True)
    image = models.ImageField(verbose_name='image', null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user"
        verbose_name_plural = "user"

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email



