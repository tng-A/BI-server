""" ValueCentre serializers"""

from rest_framework import serializers

from src.api.models.value_centre import ValueCentre
from src.api.serializers.income_stream import GraphDataSerializer

class ValueCentreSerializer(serializers.ModelSerializer):
    """ ValueCentre model serializer"""
    company = serializers.SerializerMethodField()
    number_of_transactions = serializers.IntegerField(read_only=True)
    transactions_value = serializers.FloatField(read_only=True)
    total_target = serializers.FloatField(read_only=True)
    achievement_percentage = serializers.FloatField(read_only=True)
    graph_data = GraphDataSerializer(many=True, read_only=True)

    def get_company(self, obj):
        return obj.company.name

    class Meta:
        """ Meta options"""
        
        model = ValueCentre
        fields = [ 'id', 'name', 'color', 'company',
            'number_of_transactions', 'total_target',
            'achievement_percentage', 'transactions_value', 'graph_data',]


class ValueCentreMinimalSerializer(serializers.ModelSerializer):
    """ ValueCentre model serializer"""

    class Meta:
        """ Meta options"""
        
        model = ValueCentre
        fields = ['id', 'name', 'description', 'color']
