""" Product serializers"""

from rest_framework import serializers

from src.api.models.product import Product
from src.api.serializers.income_stream import GraphDataSerializer



class ProductSerializer(serializers.ModelSerializer):
    """ Product model serializer"""

    value_centre = serializers.SerializerMethodField()
    number_of_transactions = serializers.IntegerField(read_only=True)
    transactions_value = serializers.FloatField(read_only=True)
    total_target = serializers.FloatField(read_only=True)
    achievement_percentage = serializers.FloatField(read_only=True)
    graph_data = GraphDataSerializer(many=True, read_only=True)
    

    def get_value_centre(self, obj):
        return obj.value_centre.name

    class Meta:
        """ Meta options"""
        
        model = Product
        fields = ['id', 'name', 'value_centre', 'color', 'number_of_transactions', 'total_target',
            'achievement_percentage', 'transactions_value', 'graph_data']
