""" RevenueStream serializers"""

from rest_framework import serializers

from src.api.models.revenue_stream import RevenueStream
from .income_stream import GraphDataSerializer

class RevenueStreamSerializer(serializers.ModelSerializer):
    """ RevenueStream model serializer"""

    number_of_transactions = serializers.IntegerField(read_only=True)
    transactions_value = serializers.FloatField(read_only=True)
    total_target = serializers.FloatField(read_only=True)
    achievement_percentage = serializers.FloatField(read_only=True)
    graph_data = GraphDataSerializer(many=True, read_only=True)


    class Meta:
        """ Meta options"""
        
        model = RevenueStream
        fields = ['id', 'name', 'color', 'number_of_transactions', 'total_target',
            'achievement_percentage', 'transactions_value', 'graph_data']



