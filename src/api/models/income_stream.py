""" IncomeStream model """

from django.db import models

from .base import CommonFieldsMixin
from .revenue_stream import RevenueStream

class IncomeStream(CommonFieldsMixin):
    """ IncomeStream model 
    e.g parking or evening prepaid or postpaid payments"""

    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name
