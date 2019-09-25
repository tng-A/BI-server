""" RevenueStream views"""

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.revenue_stream import RevenueStreamSerializer
from src.api.models import (
    RevenueStream,
    Product,
    Transaction
)
from src.api.helpers.transactions import IncomeStreamTransactionsFilter
from src.api.helpers.check_resource import resource_exists


class RevenueStreamListAPIView(ListAPIView):
    """ List revenue streams and transactions data"""
    serializer_class = RevenueStreamSerializer
    queryset = RevenueStream.objects.all()

    def list(self, request, *args, **kwargs):
        product = resource_exists(Product, kwargs['product_id'])
        if not product:
            message = 'Product does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        revenue_streams = product.revenue_streams.all()
        period_type = kwargs['period_type'].lower()
        year = int(kwargs['year'])
        for revenue_stream in revenue_streams:
            transactions = Transaction.objects.filter(
                income_stream__revenue_stream=revenue_stream
            ).values('amount', 'date_paid')
            if period_type == 'past_week' or period_type == 'past_month':
                    targets = revenue_stream.targets.filter(
                        period__year__contains=kwargs['year'])
            else:
                targets = revenue_stream.targets.filter(
                period__period_type__icontains=period_type,
                period__year__contains=kwargs['year']
                )
            (
            percentage,
            transactions_value,
            total_target,
            number_of_transactions,
            g_data
            ) = IncomeStreamTransactionsFilter.get_transactions_data(
                period_type, transactions, targets, year)
            revenue_stream.transactions_value = transactions_value
            revenue_stream.number_of_transactions = number_of_transactions
            revenue_stream.total_target = total_target
            revenue_stream.achievement_percentage = percentage
            revenue_stream.graph_data = g_data
        serializer = self.get_serializer(revenue_streams, many=True)
        return Response(serializer.data)



class RevenueStreamCreateAPIView(CreateAPIView):
    """ Create a revenue stream"""
    serializer_class = RevenueStreamSerializer
    queryset = RevenueStream.objects.all()
    
    def create(self, request, *args, **kwargs):
        product = resource_exists(Product, kwargs['product_id'])
        if not product:
            message = 'Product does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        exists = RevenueStream.objects.all().filter(
            name__icontains=data['name'],
            product__name__iexact=product.name
        )
        if len(exists) > 0:
            message = 'That revenue stream already exists'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer_context = {
            'request': request,
            'product': product
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(product=product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
