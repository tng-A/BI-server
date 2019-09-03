""" Target views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
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


class IncomeStreamTargetListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = IncomeStreamTargetSerializer
    queryset = IncomeStreamTarget.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            income_stream = IncomeStream.objects.get(pk=kwargs['income_stream_id'])
        except IncomeStream.DoesNotExist:
            message = 'IncomeStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = income_stream.targets.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
    def create(self, request, *args, **kwargs):
        try:
            income_stream = IncomeStream.objects.get(pk=kwargs['income_stream_id'])
        except IncomeStream.DoesNotExist:
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
            target_exists = IncomeStreamTarget.objects.get(
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
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = RevenueStreamTargetSerializer
    queryset = RevenueStreamTarget.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            revenue_stream = RevenueStream.objects.get(pk=self.kwargs['revenue_stream_id'])
        except RevenueStream.DoesNotExist:
            message = 'RevenueStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = revenue_stream.targets.all()
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
        period, _ = Period.objects.get_or_create(
            name=data.pop('period_name'),
            period_type=data.pop('period_type'),
            year=data.pop('period_year')
        )
        try:
            target_exists = RevenueStreamTarget.objects.get(
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
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ProductTargetSerializer
    queryset = ProductTarget.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(pk=self.kwargs['product_id'])
        except Product.DoesNotExist:
            message = 'Product does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = product.targets.all()
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
        period, _ = Period.objects.get_or_create(
            name=data.pop('period_name'),
            period_type=data.pop('period_type'),
            year=data.pop('period_year')
        )
        try:
            target_exists = ProductTarget.objects.get(
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
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ValueCentreTargetSerializer
    queryset = ValueCentreTarget.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            value_centre = ValueCentre.objects.get(pk=self.kwargs['value_centre_id'])
        except ValueCentre.DoesNotExist:
            message = 'ValueCentre does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = value_centre.targets.all()
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
        period, _ = Period.objects.get_or_create(
            name=data.pop('period_name'),
            period_type=data.pop('period_type'),
            year=data.pop('period_year')
        )
        try:
            target_exists = ValueCentreTarget.objects.get(
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
