""" ValueCentre model """

from django.db import models

from .base import CommonFieldsMixin
from .company import Company
from src.api.helpers.colors import generate_random_color


class ValueCentre(CommonFieldsMixin):
    """ ValueCentre model"""

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='value_centres'
    )
    color = models.CharField(
        max_length=255,
        blank=True,
        help_text='Default color associated with this value centre. Important for display in graphical representations.',
        default=generate_random_color
    )

    def __str__(self):
        return self.name
