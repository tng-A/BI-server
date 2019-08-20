""" Objectivekeyresults serializers"""

from rest_framework import serializers

from src.api.models.okr import (
    ValueCentreOKR,
    ProductOKR,
    IncomeStreamOKR,
    RevenueStreamOKR
)
from src.api.serializers.transaction import TransactionSerializer


class FilteredValueCentresOKRSSerializer(serializers.Serializer):
    label = serializers.CharField()
    value_centre = serializers.CharField()
    amount = serializers.IntegerField()

    class Meta:
        fields = ['value_centre', 'label', 'amount']


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
        fields = ['label', 'metric',
                    'revenue_stream', 'amount',]


class ValueCentreOKRSerializer(serializers.ModelSerializer):
    """ ValueCentreOKR serializer"""

    value_centre = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()
    label = serializers.CharField()

    def get_value_centre(self, obj):
        return obj.value_centre.name

    def get_metric(self, obj):
        return obj.metric.name


    class Meta:
        """ Meta options"""
        model = ValueCentreOKR
        fields = ['label', 'metric',
                    'value_centre', 'amount']


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
        fields = ['label', 'metric',
                    'product', 'amount']

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
        fields = ['label', 'metric',
                    'income_stream', 'amount']
