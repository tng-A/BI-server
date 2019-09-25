""" Metric model """

from django.db import models

from .base import CommonFieldsMixin
from .company import Company

class Metric(CommonFieldsMixin):
    """ Metric model """
    name = models.CharField(max_length=20, null=False, default='KSH')
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='metrics'
    )

    def __str__(self):
        return self.name
    
    