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
    Company,
    Transaction
)
from src.api.helpers.transactions import IncomeStreamTransactionsFilter


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
            transactions = Transaction.objects.filter(
                income_stream__revenue_stream__product__value_centre=value_centre
            ).values('amount', 'date_paid')
            if period_type == 'past_week' or period_type == 'past_month':
                targets = value_centre.targets.filter(
                    period__year__contains=kwargs['year'])
            else:
                targets = value_centre.targets.filter(
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
            value_centre.transactions_value = transactions_value
            value_centre.number_of_transactions = number_of_transactions
            value_centre.total_target = total_target
            value_centre.achievement_percentage = percentage
            value_centre.graph_data = g_data
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
