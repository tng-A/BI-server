""" RevenueStream serializers"""

from rest_framework import serializers

from src.api.models.revenue_stream import RevenueStream

class RevenueStreamSerializer(serializers.ModelSerializer):
    """ RevenueStream model serializer"""

    product = serializers.SerializerMethodField()

    def get_product(self, obj):
        return obj.product.name


    class Meta:
        """ Meta options"""
        
        model = RevenueStream
        fields = ['id', 'name', 'product']
