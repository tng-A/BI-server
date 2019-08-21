""" IncomeStream views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.income_stream import IncomeStreamSerializer
from src.api.helpers.transactions import get_transactions, months_generator
from src.api.models import (
    IncomeStream,
    RevenueStream
)


class IncomeStreamListAPIView(ListAPIView):
    """ Get all income streams (eg Parking) in a revenue stream
        (eg Embu) and transactions info
    """
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = IncomeStreamSerializer
    queryset = IncomeStream.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            revenue_stream = RevenueStream.objects.get(pk=kwargs['revenue_stream_id'])
        except RevenueStream.DoesNotExist:
            message = 'RevenueStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        get_transactions(revenue_stream)
        income_streams = revenue_stream.income_streams.all()
        months = months_generator(int(kwargs['year']))
        for income_stream in income_streams:
            transactions_value = 0
            number_of_transactions = 0
            transactions = income_stream.transactions.filter(
                date_paid__contains=kwargs['year'])
            income_stream.transactions.set(transactions)
            for transaction in transactions:
                transactions_value += transaction.amount
                number_of_transactions += 1
            g_data = []
            if len(transactions) > 0:
                for month in months:
                    current_month = months.index(month) + 1
                    value = 0
                    for t in transactions:
                        transaction_month = int(t.date_paid[5:7])
                        if current_month == transaction_month:
                            value += t.amount
                    g_data_obj = {
                        "value": value,
                        "label": month
                    }
                    g_data.append(g_data_obj)
            income_stream.transactions_value = transactions_value
            income_stream.number_of_transactions = number_of_transactions
            income_stream.graph_data = g_data
        serializer = self.get_serializer(income_streams, many=True)
        return Response(serializer.data)
