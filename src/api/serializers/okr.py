""" Objectivekeyresults serializers"""

from rest_framework import serializers

from src.api.models.okr import (
    ValueCentreOKR,
    ProductOKR,
    IncomeStreamOKR,
    DepartmentOKR,
    RevenueTypeOKR,
    RevenueStreamOKR
)


class RevenueStreamOKRSerializer(serializers.ModelSerializer):
    """ RevenueStreamOKR serializer"""

    revenue_stream = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()

    def get_revenue_stream(self, obj):
        return obj.revenue_stream.name

    def get_metric(self, obj):
        return obj.metric.name


    class Meta:
        """ Meta options"""
        model = RevenueStreamOKR
        fields = ['name', 'description', 'metric',
                    'revenue_stream', 'amount', 'period']


class RevenueTypeOKRSerializer(serializers.ModelSerializer):
    """ RevenueTypeOKR serializer"""

    revenue_type = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()

    def get_revenue_type(self, obj):
        return obj.revenue_type.name

    def get_metric(self, obj):
        return obj.metric.name


    class Meta:
        """ Meta options"""
        model = RevenueTypeOKR
        fields = ['name', 'description', 'metric',
                    'revenue_type', 'amount', 'period']



class DepartmentOKRSerializer(serializers.ModelSerializer):
    """ DepartmentOKR serializer"""

    department = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()

    def get_department(self, obj):
        return obj.department.name

    def get_metric(self, obj):
        return obj.metric.name


    class Meta:
        """ Meta options"""
        model = DepartmentOKR
        fields = ['name', 'description', 'metric',
                    'department', 'amount', 'period']


class ValueCentreOKRSerializer(serializers.ModelSerializer):
    """ ValueCentreOKR serializer"""

    value_centre = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()

    def get_value_centre(self, obj):
        return obj.value_centre.name

    def get_metric(self, obj):
        return obj.metric.name


    class Meta:
        """ Meta options"""
        model = ValueCentreOKR
        fields = ['name', 'description', 'metric',
                    'value_centre', 'amount', 'period']


class ProductOKRSerializer(serializers.ModelSerializer):
    """ ProductOKR serializer"""

    product = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()

    def get_product(self, obj):
        return obj.product.name

    def get_metric(self, obj):
        return obj.metric.name


    class Meta:
        """ Meta options"""
        model = ProductOKR
        fields = ['name', 'description', 'metric',
                    'product', 'amount', 'period']

class IncomeStreamOKRSerializer(serializers.ModelSerializer):
    """ IncomeStreamOKR serializer"""

    income_stream = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()

    def get_income_stream(self, obj):
        return obj.income_stream.name

    def get_metric(self, obj):
        return obj.metric.name


    class Meta:
        """ Meta options"""
        model = IncomeStreamOKR
        fields = ['name', 'description', 'metric',
                    'income_stream', 'amount', 'period']
