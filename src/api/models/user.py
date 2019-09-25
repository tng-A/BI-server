""" Authentication file"""

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.hashers import make_password

from src.api.models.base import CommonFieldsMixin
from .company import Company


class MyUserManager(BaseUserManager):
    
    def create_user(self, company, username, email, password=None):
        phash = make_password(password)
        user = self.model(
            company=company, username=username, email=email, password=phash
        )
        user.active = True
        user.deleted = False
        user.save()
        return user

    def create_superuser(self, username, email, password):
        phash = make_password(password)
        user = self.model(
            username=username, email=email, password=phash
        )
        user.active = True
        user.deleted = False
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    deleted = models.BooleanField(
        default=False,
        help_text='Toogle to prevent actual deletes'
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='users',
        null=True,
        blank=True
    )
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
