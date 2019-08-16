""" Objective Key Result models """

from django.db import models

from .base import CommonFieldsMixin
from .value_centre import ValueCentre
from .metric import Metric
from .product import Product
from .income_stream import IncomeStream
from .department import Department
from .revenue_stream import RevenueStream
from .revenue_type import RevenueType
from .period import Period

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
    period = models.ForeignKey(
        Period,
        on_delete=models.PROTECT,
        max_length=100,
        blank=False
    )

    def __str__(self):
        return self.name


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


class DepartmentOKR(OKRMixin):
    department = models.ForeignKey(
        Department,
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


class RevenueTypeOKR(OKRMixin):
    revenue_type = models.ForeignKey(
        RevenueType,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='okrs'
    )
