""" IncomeStream views"""

import datetime

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.income_stream import IncomeStreamSerializer
from src.api.helpers.transactions import IncomeStreamTransactionsFilter
from src.api.helpers.percentage import get_percentage
from src.api.helpers.check_resource import resource_exists
from src.api.models import (
    IncomeStream,
    RevenueStream,
    Transaction
)


class IncomeStreamListAPIView(ListAPIView):
    """ Get all incomestreams (eg Parking) in a
        revenue stream(eg Embu) and transactions info."""
    serializer_class = IncomeStreamSerializer
    queryset = IncomeStream.objects.all()

    def list(self, request, *args, **kwargs):
        revenue_stream = resource_exists(RevenueStream, kwargs['revenue_stream_id'])
        if not revenue_stream:
            message = 'RevenueStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        income_streams = revenue_stream.income_streams.all()
        period_type = kwargs['period_type'].lower()
        year = int(kwargs['year'])
        for income_stream in income_streams:
            transactions = Transaction.objects.filter(
                income_stream=income_stream
            ).values('amount', 'date_paid')
            targets = income_stream.targets.filter(
                period__period_type__icontains=period_type,
                period__year__contains=kwargs['year']
            )
            if period_type == 'past_week' or period_type == 'past_month':
                targets = income_stream.targets.filter(
                    period__year__contains=kwargs['year'])
            (
            percentage,
            transactions_value,
            total_target,
            number_of_transactions,
            g_data
            ) = IncomeStreamTransactionsFilter.get_transactions_data(
                period_type, transactions, targets, year)
            income_stream.transactions_value = transactions_value
            income_stream.number_of_transactions = number_of_transactions
            income_stream.total_target = total_target
            income_stream.achievement_percentage = percentage
            income_stream.graph_data = g_data
        serializer = self.get_serializer(income_streams, many=True)
        return Response(serializer.data)
