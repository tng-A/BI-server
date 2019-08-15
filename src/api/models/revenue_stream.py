""" RevenueStream model """

from django.db import models

from .base import CommonFieldsMixin
from .revenue_type import RevenueType

class RevenueStream(CommonFieldsMixin):
    """ RevenueStream model 
    e.g meru for county revenue type or KPLC for billable revenue type"""

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    revenue_type = models.ForeignKey(
        RevenueType,
        on_delete=models.CASCADE,
        related_name='revenue_streams'
    )

    def __str__(self):
        return self.name
