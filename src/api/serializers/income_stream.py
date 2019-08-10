""" IncomeStream serializers"""

from rest_framework import serializers

from src.api.models.income_stream import IncomeStream
from src.api.serializers.product import ProductSerializer

class IncomeStreamSerializer(serializers.ModelSerializer):
    """ IncomeStream model serializer"""

    product = ProductSerializer(read_only=True)

    class Meta:
        """ Meta options"""
        
        model = IncomeStream
        fields = ['name', 'description', 'product']
