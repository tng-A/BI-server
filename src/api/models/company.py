""" Company model """

from django.db import models

from .base import CommonFieldsMixin


class Company(CommonFieldsMixin):
    """ Company model """
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
