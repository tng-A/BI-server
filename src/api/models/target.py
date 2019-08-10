""" Target model """

from django.db import models

from .base import CommonFieldsMixin
from .metric import Metric
from .company import Company
from .value_centre import ValueCentre
from .product import Product
from .income_stream import IncomeStream


class Target(CommonFieldsMixin):
    """ Target model """

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    metric = models.OneToOneField(Metric, on_delete=models.PROTECT)
    amount = models.IntegerField()
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='targets'
    )
    value_centre = models.ForeignKey(
        ValueCentre,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='targets'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='targets'
    )
    income_stream = models.ForeignKey(
        IncomeStream,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='targets'
    )
