""" Product model """

from django.db import models

from .base import CommonFieldsMixin
from .department import Department

class Product(CommonFieldsMixin):
    """ Product model e.g agency or merchant"""

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='products'
    )
