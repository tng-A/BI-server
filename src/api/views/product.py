""" Product views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.product import ProductSerializer
from src.api.models import (
    ValueCentre,
    Product
)
from src.api.helpers.transactions import (
    get_transactions,
    IncomeStreamTransactionsFilter
)

class ProductListAPIView(ListAPIView):
    """ List products and transactions data"""
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            value_centre = ValueCentre.objects.get(pk=kwargs['value_centre_id'])
        except ValueCentre.DoesNotExist:
            message = 'ValueCentre does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        products = value_centre.products.all()
        period_type = kwargs['period_type'].lower()
        year = int(kwargs['year'])
        for product in products:
            transactions = []
            targets = []
            revenue_streams = product.revenue_streams.all()
            for revenue_stream in revenue_streams:
                get_transactions(revenue_stream)
                income_streams = revenue_stream.income_streams.all()
                for income_stream in income_streams:
                    transactions += income_stream.transactions.all()
                    # TODO , CALCULATE TARGETS AT PRODUCT LEVEL
                    if period_type == 'past_week' or period_type == 'past_month':
                        targets += income_stream.targets.filter(
                            period__year__contains=kwargs['year'])
                    else:
                        targets += income_stream.targets.filter(
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
            product.transactions_value = transactions_value
            product.number_of_transactions = number_of_transactions
            product.total_target = total_target
            product.achievement_percentage = percentage
            product.graph_data = g_data
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)



class ProductCreateAPIView(CreateAPIView):
    """ Create product"""
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    def create(self, request, *args, **kwargs):
        try:
            value_centre = ValueCentre.objects.get(pk=kwargs['value_centre_id'])
        except ValueCentre.DoesNotExist:
            message = 'ValueCentre does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        exists = Product.objects.all().filter(
            name__icontains=data['name'],
            value_centre__name__iexact=value_centre.name
        )
        if len(exists) > 0:
            message = 'That product already exists'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer_context = {
            'request': request,
            'value_centre': value_centre
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(value_centre=value_centre)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
