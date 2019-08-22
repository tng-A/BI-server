""" Target model """

from django.db import models

from .base import CommonFieldsMixin
from .metric import Metric
from .company import Company
from .value_centre import ValueCentre
from .product import Product
from .income_stream import IncomeStream
from .revenue_stream import RevenueStream
from .period import Period


class ObjectiveMixin(CommonFieldsMixin):
    amount = models.IntegerField(null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
        
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
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='value_centre_metrics'
    )
    period = models.ForeignKey(
        Period,
        on_delete=models.PROTECT,
        related_name='value_centre_periods'
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
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='product_targets'
    )
    period = models.ForeignKey(
        Period,
        on_delete=models.PROTECT,
        related_name='product_periods'
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
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='revenue_stream_targets'
    )
    period = models.ForeignKey(
        Period,
        on_delete=models.PROTECT,
        related_name='revenue_stream_periods'
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
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='income_streams'
    )
    period = models.ForeignKey(
        Period,
        on_delete=models.PROTECT,
        related_name='income_streams'
    )

    def __str__(self):
        return '{} {}'.format(self.period.name, self.period.year)
