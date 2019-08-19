""" Objective Key Result models """

from django.db import models

from .base import CommonFieldsMixin
from .value_centre import ValueCentre
from .metric import Metric
from .product import Product
from .income_stream import IncomeStream
from .revenue_stream import RevenueStream

class OKRMixin(CommonFieldsMixin):
    amount = models.IntegerField(null=False, blank=False)
    metric = models.ForeignKey(
        Metric,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )
    label = models.CharField(max_length=100, default='Jan')

    def __str__(self):
        return self.label

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


class RevenueStreamOKR(OKRMixin):
    revenue_stream = models.ForeignKey(
        RevenueStream,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='okrs'
    )
