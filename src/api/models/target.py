""" Target model """

from django.db import models

from .base import CommonFieldsMixin
from .metric import Metric
from .company import Company
from .value_centre import ValueCentre
from .product import Product
from .income_stream import IncomeStream
from .department import Department
from .revenue_type import RevenueType
from .revenue_stream import RevenueStream

class ObjectiveMixin(CommonFieldsMixin):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    amount = models.IntegerField(null=False, blank=False)
    start = models.CharField(max_length=100, null=False, blank=False)
    end = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        abstract = True


class ValueCentreTarget(ObjectiveMixin):
    value_centre = models.ForeignKey(
        ValueCentre,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='targets'
    )
    metric = models.ForeignKey(
        Metric,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='value_centre_targets'
    )
  
    
class DepartmentTarget(ObjectiveMixin):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='targets'
    )
    metric = models.ForeignKey(
        Metric,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='department_targets'
    )


class ProductTarget(ObjectiveMixin):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='targets'
    )
    metric = models.ForeignKey(
        Metric,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='product_targets'
    )


class RevenueTypeTarget(ObjectiveMixin):
    revenue_type = models.ForeignKey(
        RevenueType,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='targets'
    )
    metric = models.ForeignKey(
        Metric,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='revenue_type_targets'
    )


class RevenueStreamTarget(ObjectiveMixin):
    revenue_stream = models.ForeignKey(
        RevenueStream,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='targets'
    )
    metric = models.ForeignKey(
        Metric,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='revenue_stream_targets'
    )


class IncomeStreamTarget(ObjectiveMixin):
    income_stream = models.ForeignKey(
        IncomeStream,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='targets'
    )
    metric = models.ForeignKey(
        Metric,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='income_stream_targets'
    )
