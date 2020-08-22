from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    location = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email address', max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user"
        verbose_name_plural = "user"

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

        # TODO create a super user