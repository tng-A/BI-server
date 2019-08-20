""" Product model """

from django.db import models

from .base import CommonFieldsMixin
from .value_centre import ValueCentre
from src.api.helpers.colors import generate_random_color


class Product(CommonFieldsMixin):
    """ Product model e.g agency or merchant"""

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    value_centre = models.ForeignKey(
        ValueCentre,
        on_delete=models.CASCADE,
        related_name='products'
    )
    color = models.CharField(
        max_length=255,
        blank=True,
        help_text='Default color associated with this product.',
        default=generate_random_color
    )
    

    def __str__(self):
        return self.name
