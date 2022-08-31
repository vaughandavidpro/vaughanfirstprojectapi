from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser,PermissionsMixin

class User(AbstractUser,PermissionsMixin):
    username = models.CharField(max_length=50,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=194,unique=True)
    phone_number = PhoneNumberField(null=False,unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name']


    def __str__(self):
        return f'User {self.first_name} {self.last_name}'
