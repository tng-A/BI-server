""" Channel model """

from django.db import models

from .base import CommonFieldsMixin


class Channel(CommonFieldsMixin):
    """ Channel model 
    e.g Bank """
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name
