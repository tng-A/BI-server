""" Product serializers"""

from rest_framework import serializers

from src.api.models.product import Product
from src.api.serializers.revenue_stream import RevenueStreamSerializer


class ProductSerializer(serializers.ModelSerializer):
    """ Product model serializer"""

    value_centre = serializers.SerializerMethodField()
    revenue_stream_data = RevenueStreamSerializer(many=True, read_only=True)
    

    def get_value_centre(self, obj):
        return obj.value_centre.name

    class Meta:
        """ Meta options"""
        
        model = Product
        fields = ['id', 'name', 'description', 'value_centre',
                'revenue_stream_data']
