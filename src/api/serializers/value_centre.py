""" ValueCentre serializers"""

from rest_framework import serializers

from src.api.models.value_centre import ValueCentre
from src.api.serializers.company import CompanySerializer

class ValueCentreSerializer(serializers.ModelSerializer):
    """ ValueCentre model serializer"""

    company = CompanySerializer(read_only=True)

    class Meta:
        """ Meta options"""
        
        model = ValueCentre
        fields = ['name', 'description', 'company']
