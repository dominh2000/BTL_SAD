from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    genderChoice = ((0, "Nam"), (1, "Nữ"))
    tel = models.CharField(default='', max_length=13)
    dOB = models.DateTimeField(auto_now_add=True)
    sex = models.IntegerField(choices=genderChoice, default=0)


class Customer(User):
    nickname = models.CharField(default='', max_length=100)


class Employee(User):
    role = models.CharField(default='', max_length=256)