from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models




class CustomUserManager(BaseUserManager):
    def create_user(self,email,password ,**extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password ,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email,password,**extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(max_length=90,unique=True)
    phone_number = PhoneNumberField(null = False , unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return f"<User - {self.email}>"

