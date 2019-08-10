""" Metric model """

from django.db import models

from .base import CommonFieldsMixin

class Metric(CommonFieldsMixin):
    """ Metric model """
    name = models.CharField(max_length=20, null=False, default='KSH')
    