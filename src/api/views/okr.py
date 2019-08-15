""" OKR views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.okr import (
    ValueCentreOKRSerializer,
    ProductOKRSerializer,
    IncomeStreamOKRSerializer,
    DepartmentOKRSerializer,
    RevenueStreamOKRSerializer,
    RevenueTypeOKRSerializer
)
from src.api.models import (
    ValueCentreOKR,
    ProductOKR,
    IncomeStreamOKR,
    IncomeStream,
    ValueCentre,
    Metric,
    Product,
    Department,
    RevenueStream,
    RevenueType,
    DepartmentOKR,
    RevenueStreamOKR,
    RevenueTypeOKR
)



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


class DepartmentOKRListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = DepartmentOKRSerializer
    queryset = DepartmentOKR.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            department = Department.objects.get(pk=kwargs['department_id'])
        except Department.DoesNotExist:
            message = 'Department does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = department.okrs.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
    def create(self, request, *args, **kwargs):
        try:
            department = Department.objects.get(pk=kwargs['department_id'])
        except Department.DoesNotExist:
            message = 'Department does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        metric, _ = Metric.objects.get_or_create(name=data['metric'])
        serializer_context = {
            'request': request,
            'metric': metric,
            'department': department
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(department=department, metric=metric)
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


class RevenueTypeOKRListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = RevenueTypeOKRSerializer
    queryset = RevenueTypeOKR.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            revenue_type = RevenueType.objects.get(pk=kwargs['revenue_type_id'])
        except RevenueType.DoesNotExist:
            message = 'RevenueType does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = revenue_type.okrs.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        try:
            revenue_type = RevenueType.objects.get(pk=kwargs['revenue_type_id'])
        except RevenueType.DoesNotExist:
            message = 'RevenueType does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        metric, _ = Metric.objects.get_or_create(name=data['metric'])
        serializer_context = {
            'request': request,
            'metric': metric,
            'revenue_type': revenue_type
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(revenue_type=revenue_type, metric=metric)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
