""" Transaction views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.transaction import TransactionSerializer
from src.api.serializers.revenue_stream import RevenueStreamSerializer
from src.api.models import (
    Transaction,
    Company,
    RevenueStream
)

class TransactionListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            revenue_stream = RevenueStream.objects.get(pk=kwargs['revenue_stream_id'])
        except RevenueStream.DoesNotExist:
            message = 'RevenueStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        transactions = revenue_stream.transactions.all()
        serializer = self.get_serializer(transactions, many=True)
        return Response(serializer.data) 

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            revenue_stream = RevenueStream.objects.get(pk=kwargs['revenue_stream_id'])
        except RevenueStream.DoesNotExist:
            message = 'RevenueStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        serializer_context = {
            'request': request,
            'revenue_stream': revenue_stream
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(revenue_stream=revenue_stream)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CompanyRevenueStreams(ListAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = RevenueStreamSerializer
    queryset = RevenueStream.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            company = Company.objects.get(pk=kwargs['company_id'])
        except Company.DoesNotExist:
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

