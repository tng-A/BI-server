""" RevenueStream model """

from django.db import models

from .base import CommonFieldsMixin
from .product import Product
from src.api.helpers.colors import generate_random_color


class RevenueStream(CommonFieldsMixin):
    """ RevenueStream model 
    e.g meru for county revenue stream"""

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='revenue_streams'
    )
    color = models.CharField(
        max_length=255,
        blank=True,
        help_text='Default color associated with this revenue stream.',
        default=generate_random_color
    )

    def __str__(self):
        return self.name
