""" Target views"""

from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.target import (
    ValueCentreTargetSerializer,
    ProductTargetSerializer,
    IncomeStreamTargetSerializer,
    RevenueStreamTargetSerializer
)
from src.api.models import (
    ValueCentreTarget,
    ProductTarget,
    IncomeStreamTarget,
    IncomeStream,
    ValueCentre,
    Metric,
    Product,
    RevenueStream,
    RevenueStreamTarget,
    Period
)
from src.api.helpers.check_resource import resource_exists


class IncomeStreamTargetListCreateAPIView(ListCreateAPIView):
    serializer_class = IncomeStreamTargetSerializer
    queryset = IncomeStreamTarget.objects.all()

    def list(self, request, *args, **kwargs):
        income_stream = resource_exists(IncomeStream, kwargs['income_stream_id'])
        if not income_stream:
            message = 'IncomeStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = income_stream.targets.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
    def create(self, request, *args, **kwargs):
        income_stream = resource_exists(IncomeStream, kwargs['income_stream_id'])
        if not income_stream:
            message = 'IncomeStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        metric, _ = Metric.objects.get_or_create(name=data['metric'])
        period, _ = Period.objects.get_or_create(
            name=data.pop('period_name'),
            period_type=data.pop('period_type'),
            year=data.pop('period_year')
        )
        try:
            target_exists = income_stream.targets.get(
                metric=metric,
                period=period,
            )
        except:
            target_exists = None
        if target_exists:
            message = 'IncomeStreamTarget already exists'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer_context = {
            'request': request,
            'metric': metric,
            'income_stream': income_stream,
            'period': period
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(income_stream=income_stream, metric=metric, period=period)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RevenueStreamTargetListCreateAPIView(ListCreateAPIView):
    serializer_class = RevenueStreamTargetSerializer
    queryset = RevenueStreamTarget.objects.all()

    def list(self, request, *args, **kwargs):
        revenue_stream = resource_exists(RevenueStream, kwargs['revenue_stream_id'])
        if not revenue_stream:
            message = 'RevenueStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = revenue_stream.targets.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
    def create(self, request, *args, **kwargs):
        revenue_stream = resource_exists(RevenueStream, kwargs['revenue_stream_id'])
        if not revenue_stream:
            message = 'RevenueStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        metric, _ = Metric.objects.get_or_create(name=data['metric'])
        period, _ = Period.objects.get_or_create(
            name=data.pop('period_name'),
            period_type=data.pop('period_type'),
            year=data.pop('period_year')
        )
        try:
            target_exists = revenue_stream.targets.get(
                metric=metric,
                period=period,
            )
        except:
            target_exists = None
        if target_exists:
            message = 'RevenueStreamTarget already exists'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer_context = {
            'request': request,
            'metric': metric,
            'revenue_stream': revenue_stream,
            'period': period
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(revenue_stream=revenue_stream, metric=metric, period=period)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductTargettListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductTargetSerializer
    queryset = ProductTarget.objects.all()

    def list(self, request, *args, **kwargs):
        product = resource_exists(Product, kwargs['product_id'])
        if not product:
            message = 'Product does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = product.targets.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        product = resource_exists(Product, kwargs['product_id'])
        if not product:
            message = 'Product does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        metric, _ = Metric.objects.get_or_create(name=data['metric'])
        period, _ = Period.objects.get_or_create(
            name=data.pop('period_name'),
            period_type=data.pop('period_type'),
            year=data.pop('period_year')
        )
        try:
            target_exists = product.targets.get(
                metric=metric,
                period=period,
            )
        except:
            target_exists = None
        if target_exists:
            message = 'ProductTarget already exists'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer_context = {
            'request': request,
            'metric': metric,
            'product': product,
            'period': period
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(product=product, metric=metric, period=period)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ValueCentreTargetListCreateAPIView(ListCreateAPIView):
    serializer_class = ValueCentreTargetSerializer
    queryset = ValueCentreTarget.objects.all()

    def list(self, request, *args, **kwargs):
        value_centre = resource_exists(ValueCentre, kwargs['value_centre_id'])
        if not value_centre:
            message = 'ValueCentre does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = value_centre.targets.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        value_centre = resource_exists(ValueCentre, kwargs['value_centre_id'])
        if not value_centre:
            message = 'ValueCentre does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        metric, _ = Metric.objects.get_or_create(name=data['metric'])
        period, _ = Period.objects.get_or_create(
            name=data.pop('period_name'),
            period_type=data.pop('period_type'),
            year=data.pop('period_year')
        )
        try:
            target_exists = value_centre.targets.get(
                metric=metric,
                period=period,
            )
        except:
            target_exists = None
        if target_exists:
            message = 'ValueCentreTarget already exists'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer_context = {
            'request': request,
            'metric': metric,
            'value_centre': value_centre,
            'period': period
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(value_centre=value_centre, metric=metric, period=period)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
