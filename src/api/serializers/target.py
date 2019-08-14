""" Target serializers"""

from rest_framework import serializers

from src.api.models.target import (
    ValueCentreTarget,
    ProductTarget,
    IncomeStreamTarget,
    DepartmentTarget,
    RevenueStreamTarget,
    RevenueTypeTarget
)
from src.api.serializers.product import ProductSerializer
from src.api.serializers.income_stream import IncomeStreamSerializer
from src.api.serializers.metric import MetricSerializer


class ValueCentreTargetSerializer(serializers.ModelSerializer):
    """ ValueCentreTarget serializer"""

    value_centre = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()

    def get_value_centre(self, obj):
        return obj.value_centre.name

    def get_metric(self, obj):
        return obj.metric.name


    class Meta:
        """ Meta options"""
        model = ValueCentreTarget
        fields = ['name', 'description', 'metric',
                    'value_centre', 'amount', 'start', 'end']


class DepartmentTargetSerializer(serializers.ModelSerializer):
    """ DepartmentTarget serializer"""

    department = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()

    def get_department(self, obj):
        return obj.department.name

    def get_metric(self, obj):
        return obj.metric.name


    class Meta:
        """ Meta options"""
        model = DepartmentTarget
        fields = ['name', 'description', 'metric',
                    'department', 'amount', 'start', 'end']

class ProductTargetSerializer(serializers.ModelSerializer):
    """ ProductTarget serializer"""

    product = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()

    def get_product(self, obj):
        return obj.product.name

    def get_metric(self, obj):
        return obj.metric.name


    class Meta:
        """ Meta options"""
        model = ProductTarget
        fields = ['name', 'description', 'metric',
                    'product', 'amount', 'start', 'end']


class RevenueTypeTargetSerializer(serializers.ModelSerializer):
    """ RevenueTypeTarget serializer"""

    revenue_type = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()

    def get_revenue_type(self, obj):
        return obj.revenue_type.name

    def get_metric(self, obj):
        return obj.metric.name


    class Meta:
        """ Meta options"""
        model = RevenueTypeTarget
        fields = ['name', 'description', 'metric',
                    'revenue_type', 'amount', 'start', 'end']


class RevenueStreamTargetSerializer(serializers.ModelSerializer):
    """ RevenueStreamTarget serializer"""

    revenue_stream = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()

    def get_revenue_stream(self, obj):
        return obj.revenue_stream.name

    def get_metric(self, obj):
        return obj.metric.name


    class Meta:
        """ Meta options"""
        model = RevenueStreamTarget
        fields = ['name', 'description', 'metric',
                    'revenue_stream', 'amount', 'start', 'end']

class IncomeStreamTargetSerializer(serializers.ModelSerializer):
    """ IncomeStreamTarget serializer"""

    income_stream = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()

    def get_income_stream(self, obj):
        return obj.income_stream.name

    def get_metric(self, obj):
        return obj.metric.name


    class Meta:
        """ Meta options"""
        model = IncomeStreamTarget
        fields = ['name', 'description', 'metric',
                    'income_stream', 'amount', 'start', 'end']

