""" IncomeStream serializers"""

from rest_framework import serializers

from src.api.models.income_stream import IncomeStream
from src.api.serializers.revenue_stream import RevenueStreamSerializer

class IncomeStreamSerializer(serializers.ModelSerializer):
    """ IncomeStream model serializer"""

    revenue_stream = RevenueStreamSerializer(read_only=True)

    class Meta:
        """ Meta options"""
        
        model = IncomeStream
        fields = ['name', 'description', 'revenue_stream']
