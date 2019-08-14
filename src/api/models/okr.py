""" Objective Key Result models """

from django.db import models

from .base import CommonFieldsMixin
from .value_centre import ValueCentre
from .metric import Metric
from .product import Product
from .income_stream import IncomeStream


class OKRMixin(CommonFieldsMixin):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    amount = models.IntegerField(null=False, blank=False)
    metric = models.ForeignKey(
        Metric,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )
    period = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )


    class Meta:
        abstract = True


class ValueCentreOKR(OKRMixin):
    value_centre = models.ForeignKey(
        ValueCentre,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='okrs'
    )
    

class ProductOKR(OKRMixin):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='okrs'
    )


class IncomeStreamOKR(OKRMixin):
    income_stream = models.ForeignKey(
        IncomeStream,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='okrs'
    )
