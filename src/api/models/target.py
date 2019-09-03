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
        related_name='value_centres'
    )
    period = models.ForeignKey(
        Period,
        on_delete=models.PROTECT,
        related_name='value_centres'
    )

    def __str__(self):
        return '{} {}'.format(self.period.name, self.period.year)


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
        related_name='products'
    )
    period = models.ForeignKey(
        Period,
        on_delete=models.PROTECT,
        related_name='products'
    )

    def __str__(self):
        return '{} {}'.format(self.period.name, self.period.year)
    


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
        related_name='revenue_streams'
    )
    period = models.ForeignKey(
        Period,
        on_delete=models.PROTECT,
        related_name='revenue_streams'
    )

    def __str__(self):
        return '{} {}'.format(self.period.name, self.period.year)


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
