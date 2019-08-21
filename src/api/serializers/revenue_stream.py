""" RevenueStream serializers"""

from rest_framework import serializers

from src.api.models.revenue_stream import RevenueStream
from .transaction import TransactionSerializer

class RevenueStreamSerializer(serializers.ModelSerializer):
    """ RevenueStream model serializer"""

    product = serializers.SerializerMethodField()
    number_of_transactions = serializers.IntegerField()
    transactions_value = serializers.FloatField()
    transactions = TransactionSerializer(many=True)

    def get_product(self, obj):
        return obj.product.name


    class Meta:
        """ Meta options"""
        
        model = RevenueStream
        fields = ['id', 'name', 'product', 'number_of_transactions', 'transactions_value', 'transactions']
