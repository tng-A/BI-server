""" RevenueStream model """

from django.db import models

from .base import CommonFieldsMixin
from .product import Product


class RevenueStream(CommonFieldsMixin):
    """ RevenueStream model 
    e.g meru for county revenue """

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='revenue_streams'
    )

    def __str__(self):
        return self.name
