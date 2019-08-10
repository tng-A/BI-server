""" Target serializers"""

from rest_framework import serializers

from src.api.models.target import ValueCentreTarget, ProductTarget, IncomeStreamTarget
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
                    'value_centre', 'amount']


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
                    'product', 'amount']

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
                    'income_stream', 'amount']

