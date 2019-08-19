""" Product serializers"""

from rest_framework import serializers

from src.api.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    """ Product model serializer"""

    value_centre = serializers.SerializerMethodField()

    def get_value_centre(self, obj):
        return obj.value_centre.name

    class Meta:
        """ Meta options"""
        
        model = Product
        fields = ['name', 'description', 'value_centre']
