""" Authentication file"""

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.hashers import make_password

from src.api.models.base import CommonFieldsMixin

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        phash = make_password(password)
        user = self.model(email=email, password=phash)
        user.save()
        return user

    def create_superuser(self, email, password):
        phash = make_password(password)
        user = self.model(email=email, password=phash)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin, CommonFieldsMixin):
    email = models.EmailField(max_length=40, unique=True)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    class Meta:
        app_label = 'api'
