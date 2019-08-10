""" Target model """

from django.db import models

from .base import CommonFieldsMixin
from .metric import Metric
from .company import Company
from .value_centre import ValueCentre
from .product import Product
from .income_stream import IncomeStream

class ObjectiveMixin(CommonFieldsMixin):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    amount = models.IntegerField(null=False, blank=False)


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
        related_name='value_centres'
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
        related_name='products',
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
        related_name='income_streams',
    )
