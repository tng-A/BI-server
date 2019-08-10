""" Subsidiary model """

from django.db import models

from .base import CommonFieldsMixin
from .company import Company


class Subsidiary(CommonFieldsMixin):
    """ Subsidiary model """

    country = models.CharField(max_length=50, null=False)
    town = models.CharField(max_length=50, null=False)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='subsidiaries'
    )

