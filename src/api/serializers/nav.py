""" Main nav serializer"""

from rest_framework import serializers

from src.api.models import ValueCentre, Product, IncomeStream, RevenueStream
from src.api.serializers.value_centre import ValueCentreMinimalSerializer


class IncomeStreamMinimalSerializer(serializers.ModelSerializer):
    """ IncomeStream model serializer"""
    class Meta:
        """ Meta options"""
        
        model = IncomeStream
        fields = ['id', 'name', 'color']


class RevenueStreamMinimalSerializer(serializers.ModelSerializer):
    """ RevenueStream model serializer"""
    income_stream = IncomeStreamMinimalSerializer(many=True)
    visible_to = serializers.ListField()

    class Meta:
        """ Meta options"""
        
        model = RevenueStream
        fields = ['id', 'name', 'description', 'color', 'income_stream', 'visible_to']


class ProductMinimalSerializer(serializers.ModelSerializer):
    """ Product model serializer"""
    revenue_stream = RevenueStreamMinimalSerializer(many=True)
    visible_to = serializers.ListField()

    class Meta:
        """ Meta options"""
        
        model = Product
        fields = ['id', 'name', 'description', 'color', 'revenue_stream', 'visible_to']

class NavSerializer(serializers.ModelSerializer):
    """ Nav serializer"""
    product = ProductMinimalSerializer(many=True)
    visible_to = serializers.ListField()
    
    class Meta:
        """ Meta options"""
        
        model = ValueCentre
        fields = ['id', 'name', 'description', 'color', 'product', 'visible_to']
