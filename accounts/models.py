from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    phone = models.CharField()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'