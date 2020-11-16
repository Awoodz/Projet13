from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class TypeList(models.Model):
    type_name = models.CharField(max_length=15, unique=True,)


class UserType(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    usertype = models.OneToOneField(TypeList, on_delete=models.CASCADE)
