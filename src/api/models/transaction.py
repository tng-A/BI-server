""" Transactions model"""

from django.db import models

from .base import CommonFieldsMixin
from .revenue_stream import RevenueStream
from .income_stream import IncomeStream


class Transaction(CommonFieldsMixin):
    """ Transaction model"""
    date_paid = models.CharField(max_length=255)
    receipt_number = models.CharField(max_length=255, unique=True)
    amount = models.FloatField()
    income_stream = models.ForeignKey(
        IncomeStream,
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    def __str__(self):
        return '{}'.format(self.income_stream.name)
