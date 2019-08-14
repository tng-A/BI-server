""" RevenueStream serializers"""

from rest_framework import serializers

from src.api.models.revenue_stream import RevenueStream
from src.api.serializers.revenue_type import RevenueTypeSerializer

class RevenueStreamSerializer(serializers.ModelSerializer):
    """ RevenueStream model serializer"""

    revenue_type = RevenueTypeSerializer(read_only=True)

    class Meta:
        """ Meta options"""
        
        model = RevenueStream
        fields = ['name', 'description', 'revenue_type']
