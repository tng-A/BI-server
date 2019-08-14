""" IncomeStream model """

from django.db import models

from .base import CommonFieldsMixin
from .revenue_stream import RevenueStream

class IncomeStream(CommonFieldsMixin):
    """ IncomeStream model 
    e.g parking or evening prepaid or postpaid payments"""

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    revenue_stream = models.ForeignKey(
        RevenueStream,
        on_delete=models.CASCADE,
        related_name='income_streams'
    )
