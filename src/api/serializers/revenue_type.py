""" RevenueType serializers"""

from rest_framework import serializers

from src.api.models.revenue_type import RevenueType
from src.api.serializers.product import ProductSerializer

class RevenueTypeSerializer(serializers.ModelSerializer):
    """ RevenueType model serializer"""

    product = ProductSerializer(read_only=True)

    class Meta:
        """ Meta options"""
        
        model = RevenueType
        fields = ['name', 'description', 'product']
