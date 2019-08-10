""" ValueCentre serializers"""

from rest_framework import serializers

from src.api.models.value_centre import ValueCentre
from src.api.serializers.subsidiary import SubsidiarySerializer

class ValueCentreSerializer(serializers.ModelSerializer):
    """ ValueCentre model serializer"""

    subsidiary = SubsidiarySerializer(read_only=True)

    class Meta:
        """ Meta options"""
        
        model = ValueCentre
        fields = ['name', 'description', 'subsidiary']
