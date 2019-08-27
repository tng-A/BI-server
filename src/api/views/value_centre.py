""" ValueCentre views"""
from django.db.models import Sum
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.value_centre import ValueCentreSerializer
from src.api.models import (
    ValueCentre,
    Company
)
from src.api.helpers.transactions import (
    get_transactions,
    IncomeStreamTransactionsFilter
)


class ValueCentreListAPIView(ListAPIView):
    """ List value centres and their transactions data"""
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ValueCentreSerializer
    queryset = ValueCentre.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            company = Company.objects.get(pk=kwargs['company_id'])
        except Company.DoesNotExist:
            message = 'Company does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        value_centres = company.value_centres.all()
        period_type = kwargs['period_type'].lower()
        year = int(kwargs['year'])
        for value_centre in value_centres:
            products = value_centre.products.all()
            product_data = []
            for product in products:
                revenue_streams = product.revenue_streams.all()
                revenue_stream_data = []
                for revenue_stream in revenue_streams:
                    get_transactions(revenue_stream)
                    income_streams = revenue_stream.income_streams.all()
                    income_stream_transaction_data = []
                    for income_stream in income_streams:
                        transactions = income_stream.transactions.all()
                        targets = income_stream.targets.filter(
                            period__period_type__icontains=period_type,
                            period__year__contains=kwargs['year']
                        )
                        if period_type == 'past_week' or period_type == 'past_month':
                            targets = income_stream.targets.filter(
                                period__year__contains=kwargs['year'])
                        income_stream = IncomeStreamTransactionsFilter.get_transactions_data(
                            income_stream, period_type, transactions, targets, year)
                        income_stream_transaction_data.append(income_stream)
                    revenue_stream.income_stream_transaction_data = income_stream_transaction_data
                    revenue_stream_data.append(revenue_stream)
                product.revenue_stream_data = revenue_stream_data
                product_data.append(product)
                value_centre.product_data = product_data
        serializer = self.get_serializer(value_centres, many=True)
        return Response(serializer.data)


class ValueCentreCreateAPIView(CreateAPIView):
    """ Create value centre"""
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ValueCentreSerializer
    queryset = ValueCentre.objects.all()
    
    def create(self, request, *args, **kwargs):
        try:
            company = Company.objects.get(pk=kwargs['company_id'])
        except Company.DoesNotExist:
            message = 'Company does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        exists = ValueCentre.objects.all().filter(
            name__icontains=data['name'],
            company__name__iexact=company.name
        )
        if len(exists) > 0:
            message = 'That value centre already exists'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer_context = {
            'request': request,
            'company': company
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(company=company)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
