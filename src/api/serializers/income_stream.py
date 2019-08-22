""" IncomeStream serializers"""

from rest_framework import serializers

from src.api.models.income_stream import IncomeStream
from src.api.serializers.revenue_stream import RevenueStreamSerializer
from .transaction import TransactionSerializer



class GraphDataSerializer(serializers.Serializer):
    label = serializers.CharField()
    value = serializers.FloatField()

    class Meta:
        fields = '__all__'


class IncomeStreamSerializer(serializers.ModelSerializer):
    """ IncomeStream model serializer"""

    number_of_transactions = serializers.IntegerField()
    transactions_value = serializers.FloatField()
    total_target = serializers.FloatField()
    achievement_percentage = serializers.FloatField()
    graph_data = GraphDataSerializer(many=True)

    class Meta:
        """ Meta options"""
        
        model = IncomeStream
        fields = ['name', 'number_of_transactions', 'total_target',
                    'achievement_percentage', 'transactions_value', 'graph_data', 'color']
