""" Transaction views"""

from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.transaction import TransactionSerializer
from src.api.serializers.revenue_stream import RevenueStreamSerializer
from src.api.models import (
    Transaction,
    Company,
    RevenueStream,
    Product
)
from src.api.helpers.check_resource import resource_exists


class ProductTransactionsList(ListAPIView):
    """ List all transactions in a given product"""
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def list(self, request, *args, **kwargs):
        """ Get all transactions in a given product """
        product = resource_exists(Product, kwargs['product_id'])
        if not product:
            message = 'Product does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        revenue_streams = product.revenue_streams.all()
        transactions = []
        for revenue_stream in revenue_streams:
            transactions += revenue_stream.transactions.all()
        serializer = self.get_serializer(transactions, many=True)
        return Response(serializer.data)


class TransactionListCreateAPIView(ListCreateAPIView):
    """ List/Create all transaction(s) in a given revenue stream """
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    def list(self, request, *args, **kwargs):
        revenue_stream = resource_exists(RevenueStream, kwargs['revenue_stream_id'])
        if not revenue_stream:
            message = 'RevenueStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        transactions = revenue_stream.transactions.all()
        serializer = self.get_serializer(transactions, many=True)
        return Response(serializer.data) 

    def create(self, request, *args, **kwargs):
        data = request.data
        revenue_stream = resource_exists(RevenueStream, kwargs['revenue_stream_id'])
        if not revenue_stream:
            message = 'RevenueStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        try:
            channel = Channel.objects.get(pk=data.pop('channel_id'))
        except Channel.DoesNotExist:
            message = 'Channel does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        serializer_context = {
            'request': request,
            'revenue_stream': revenue_stream,
            'channel': channel
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(revenue_stream=revenue_stream, channel=channel)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CompanyRevenueStreams(ListAPIView):
    """ Get all the revenue_streams in a given company"""
    serializer_class = RevenueStreamSerializer
    queryset = RevenueStream.objects.all()

    def list(self, request, *args, **kwargs):
        company = resource_exists(Company, kwargs['company_id'])
        if not company:
            message = 'Company does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        value_centres = company.value_centres.all()
        revenue_streams = []
        for value_centre in value_centres:
            products = value_centre.products.all()
            for product in products:
                revenue_streams += product.revenue_streams.all()
        serializer = self.get_serializer(revenue_streams, many=True)
        return Response(serializer.data) 

