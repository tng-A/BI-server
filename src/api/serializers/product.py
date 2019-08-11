""" Product serializers"""

from rest_framework import serializers

from src.api.models.product import Product
from src.api.serializers.value_centre import ValueCentreSerializer

class ProductSerializer(serializers.ModelSerializer):
    """ Product model serializer"""

    value_centre = ValueCentreSerializer(read_only=True)

    class Meta:
        """ Meta options"""
        
        model = Product
        fields = ['name', 'description', 'value_centre']
