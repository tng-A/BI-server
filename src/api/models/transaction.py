""" Transactions model"""

from django.db import models

from .base import CommonFieldsMixin
from .revenue_stream import RevenueStream
from .channel import Channel


class Transaction(CommonFieldsMixin):
    transaction_id = models.UUIDField(unique=True)
    amount = models.FloatField()
    revenue_stream = models.ForeignKey(
        RevenueStream,
        on_delete=models.PROTECT,
        related_name='transactions'
    )
    channel = models.ForeignKey(
        Channel,
        on_delete=models.PROTECT,
        related_name='transactions'
    )

    def __str__(self):
        return '{}'.format(self.transaction_id)
