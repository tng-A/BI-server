""" Objectivekeyresults serializers"""

from rest_framework import serializers

from src.api.models.okr import ValueCentreOKR, ProductOKR, IncomeStreamOKR
from src.api.serializers.product import ProductSerializer
from src.api.serializers.income_stream import IncomeStreamSerializer
from src.api.serializers.metric import MetricSerializer


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
        fields = ['name', 'description', 'metric',
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
        fields = ['name', 'description', 'metric',
                    'income_stream', 'amount', 'period']
