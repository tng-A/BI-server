""" IncomeStream model """

from django.db import models

from .base import CommonFieldsMixin
from .product import Product

class IncomeStream(CommonFieldsMixin):
    """ IncomeStream model """

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    income_stream = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='income_streams'
    )
