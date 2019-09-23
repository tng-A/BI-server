""" IncomeStream serializers"""

from rest_framework import serializers

from src.api.models.income_stream import IncomeStream

class GraphDataSerializer(serializers.Serializer):
    """
    Serializer for the graph data object to help with
    displaying data on the frontend
    """
    label = serializers.CharField()
    value = serializers.FloatField()

    class Meta:
        """ Meta options"""
        fields = '__all__'


class IncomeStreamSerializer(serializers.ModelSerializer):
    """ IncomeStream model serializer"""

    number_of_transactions = serializers.IntegerField(read_only=True)
    transactions_value = serializers.FloatField(read_only=True)
    total_target = serializers.FloatField(read_only=True)
    achievement_percentage = serializers.FloatField(read_only=True)
    graph_data = GraphDataSerializer(many=True, read_only=True)

    class Meta:
        """ Meta options"""
        
        model = IncomeStream
        fields = ['id', 'name', 'number_of_transactions', 'total_target',
                    'achievement_percentage', 'transactions_value', 'graph_data', 'color']

