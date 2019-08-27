""" RevenueStream serializers"""

from rest_framework import serializers

from src.api.models.revenue_stream import RevenueStream
from .income_stream import IncomeStreamSerializer

class RevenueStreamSerializer(serializers.ModelSerializer):
    """ RevenueStream model serializer"""

    product = serializers.SerializerMethodField()
    income_stream_transaction_data = IncomeStreamSerializer(many=True)

    def get_product(self, obj):
        return obj.product.name


    class Meta:
        """ Meta options"""
        
        model = RevenueStream
        fields = ['id', 'product', 'name', 'income_stream_transaction_data']
