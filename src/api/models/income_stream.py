""" IncomeStream model """

from django.db import models

from .base import CommonFieldsMixin
from .revenue_stream import RevenueStream
from src.api.helpers.colors import generate_random_color


class IncomeStream(CommonFieldsMixin):
    """ IncomeStream model 
    e.g parking or evening prepaid or postpaid payments"""

    name = models.CharField(max_length=50, null=False)
    revenue_stream = models.ForeignKey(
        RevenueStream,
        on_delete=models.CASCADE,
        related_name='income_streams'
    )
    color = models.CharField(
        max_length=255,
        blank=True,
        help_text='Default color associated with this income stream.',
        default=generate_random_color
    )

    def __str__(self):
        return self.name
