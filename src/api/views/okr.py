""" OKR views"""
import dateutil.parser

from django.db.models import Q
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.okr import (
    ValueCentreOKRSerializer,
    ProductOKRSerializer,
    IncomeStreamOKRSerializer,
    RevenueStreamOKRSerializer,
    FilteredValueCentresOKRSSerializer,
    RevenueStreamTransactionsOKRSerializer
)
from src.api.models import (
    ValueCentreOKR,
    ProductOKR,
    IncomeStreamOKR,
    IncomeStream,
    ValueCentre,
    Metric,
    Product,
    RevenueStream,
    RevenueStreamOKR,
    Company,
    Transaction
)


class RevenueStreamTransactionsOKRListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = RevenueStreamTransactionsOKRSerializer
    queryset = Transaction.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            revenue_stream = RevenueStream.objects.get(pk=kwargs['revenue_stream_id'])
        except RevenueStream.DoesNotExist:
            message = 'RevenueStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        transactions = Transaction.objects.all().filter(
            revenue_stream__id__icontains=revenue_stream.id
        )
        transactions_value = 0
        number_of_transactions = 0
        for transaction in transactions:
            transactions_value += transaction.amount
            number_of_transactions += 1
        okr = {
            "transactions_value": transactions_value,
            "number_of_transactions": number_of_transactions,
            "transactions": transactions
        }
        serializer = self.get_serializer(okr)
        return Response(serializer.data)


class FilteredValueCentresOKRSListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ValueCentreOKRSerializer
    queryset = ValueCentreOKR.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            company = Company.objects.get(pk=kwargs['company_id'])
        except Company.DoesNotExist:
            message = 'Company does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = company.value_centres.all()
        all_okrs = []
        for v_c in queryset:
            all_okrs += v_c.okrs.filter(
                period__period_type__iexact=kwargs['period_type']
            ).filter(
                Q(period__start__icontains=kwargs['year']) |
                Q(period__end__icontains=kwargs['year']))
            for okr in all_okrs:
                start_date = okr.period.start.strftime("%b %d %Y")
                okr.label = start_date[:3]
        serializer = self.get_serializer(all_okrs, many=True)
        return Response(serializer.data)


class IncomeStreamOKRListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = IncomeStreamOKRSerializer
    queryset = IncomeStreamOKR.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            income_stream = IncomeStream.objects.get(pk=self.kwargs['income_stream_id'])
        except IncomeStream.DoesNotExist:
            message = 'IncomeStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = income_stream.okrs.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
    def create(self, request, *args, **kwargs):
        try:
            income_stream = IncomeStream.objects.get(pk=self.kwargs['income_stream_id'])
        except Product.DoesNotExist:
            message = 'IncomeStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        metric, _ = Metric.objects.get_or_create(name=data['metric'])
        serializer_context = {
            'request': request,
            'metric': metric,
            'income_stream': income_stream
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(income_stream=income_stream, metric=metric)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductOKRListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ProductOKRSerializer
    queryset = ProductOKR.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(pk=self.kwargs['product_id'])
        except Product.DoesNotExist:
            message = 'Product does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = product.okrs.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(pk=self.kwargs['product_id'])
        except Product.DoesNotExist:
            message = 'Product does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        metric, _ = Metric.objects.get_or_create(name=data['metric'])
        serializer_context = {
            'request': request,
            'metric': metric,
            'product': product
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(product=product, metric=metric)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ValueCentreOKRListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ValueCentreOKRSerializer
    queryset = ValueCentreOKR.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            value_centre = ValueCentre.objects.get(pk=self.kwargs['value_centre_id'])
        except ValueCentre.DoesNotExist:
            message = 'ValueCentre does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = value_centre.okrs.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        try:
            value_centre = ValueCentre.objects.get(pk=kwargs['value_centre_id'])
        except ValueCentre.DoesNotExist:
            message = 'ValueCentre does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        metric, _ = Metric.objects.get_or_create(name=data['metric'])
        serializer_context = {
            'request': request,
            'metric': metric,
            'value_centre': value_centre
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(value_centre=value_centre, metric=metric)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RevenueStreamOKRListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = RevenueStreamOKRSerializer
    queryset = RevenueStreamOKR.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            revenue_stream = RevenueStream.objects.get(pk=self.kwargs['revenue_stream_id'])
        except RevenueStream.DoesNotExist:
            message = 'RevenueStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = revenue_stream.okrs.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            revenue_stream = RevenueStream.objects.get(pk=self.kwargs['revenue_stream_id'])
        except RevenueStream.DoesNotExist:
            message = 'RevenueStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        metric, _ = Metric.objects.get_or_create(name=data['metric'])
        serializer_context = {
            'request': request,
            'metric': metric,
            'revenue_stream': revenue_stream
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(revenue_stream=revenue_stream, metric=metric)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
