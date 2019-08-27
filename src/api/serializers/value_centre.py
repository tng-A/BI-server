""" ValueCentre serializers"""

from rest_framework import serializers

from src.api.models.value_centre import ValueCentre
from src.api.serializers.product import ProductSerializer

class ValueCentreSerializer(serializers.ModelSerializer):
    """ ValueCentre model serializer"""
    company = serializers.SerializerMethodField()
    product_data = ProductSerializer(many=True, read_only=True)

    def get_company(self, obj):
        return obj.company.name

    class Meta:
        """ Meta options"""
        
        model = ValueCentre
        fields = [ 'id', 'name', 'color', 'company', 'product_data']
