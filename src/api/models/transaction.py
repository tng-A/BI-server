""" Transactions model"""

from django.db import models

from .base import CommonFieldsMixin
from .revenue_stream import RevenueStream
from .channel import Channel
from .income_stream import IncomeStream


class Transaction(CommonFieldsMixin):
    date_paid = models.CharField(max_length=255)
    receipt_number = models.CharField(max_length=255, unique=True)
    amount = models.FloatField()
    revenue_stream = models.ForeignKey(
        RevenueStream,
        on_delete=models.PROTECT,
        related_name='transactions'
    )
    income_stream = models.ForeignKey(
        IncomeStream,
        on_delete=models.PROTECT,
        related_name='transactions'
    )

    def __str__(self):
        return '{}'.format(self.revenue_stream.name)
