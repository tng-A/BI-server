""" ValueCentre model """

from django.db import models

from .base import CommonFieldsMixin
from .company import Company

class ValueCentre(CommonFieldsMixin):
    """ ValueCentre model"""

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='value_centres'
    )

    def __str__(self):
        return self.name
