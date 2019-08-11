""" ValueCentre model """

from django.db import models

from .base import CommonFieldsMixin
from .company import Company
from .subsidiary import Subsidiary

class ValueCentre(CommonFieldsMixin):
    """ ValueCentre model """

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    subsidiary = models.ForeignKey(
        Subsidiary,
        on_delete=models.CASCADE,
        related_name='value_centres'
    )
