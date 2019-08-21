""" RevenueStream serializers"""

from rest_framework import serializers

from src.api.models.revenue_stream import RevenueStream
from .transaction import TransactionSerializer

class RevenueStreamSerializer(serializers.ModelSerializer):
    """ RevenueStream model serializer"""

    product = serializers.SerializerMethodField()
    number_of_transactions = serializers.IntegerField(read_only=True)
    transactions_value = serializers.FloatField(read_only=True)
    transactions = TransactionSerializer(many=True, read_only=True)

    def get_product(self, obj):
        return obj.product.name


    class Meta:
        """ Meta options"""
        
        model = RevenueStream
        fields = ['id', 'name', 'product', 'number_of_transactions', 'transactions_value', 'transactions']
