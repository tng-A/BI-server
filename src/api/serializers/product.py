""" Product serializers"""

from rest_framework import serializers

from src.api.models.product import Product
from src.api.serializers.transaction import TransactionSerializer


class ProductSerializer(serializers.ModelSerializer):
    """ Product model serializer"""

    value_centre = serializers.SerializerMethodField()
    number_of_transactions = serializers.IntegerField()
    transactions_value = serializers.FloatField()
    transactions = TransactionSerializer(many=True)

    def get_value_centre(self, obj):
        return obj.value_centre.name

    class Meta:
        """ Meta options"""
        
        model = Product
        fields = ['name', 'description', 'value_centre',
                'number_of_transactions', 'transactions_value', 'transactions']
