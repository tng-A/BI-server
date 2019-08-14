""" Department serializers"""

from rest_framework import serializers

from src.api.models.department import Department
from src.api.serializers.value_centre import ValueCentreSerializer

class DepartmentSerializer(serializers.ModelSerializer):
    """ Department model serializer"""

    value_centre = ValueCentreSerializer(read_only=True)

    class Meta:
        """ Meta options"""
        
        model = Department
        fields = ['name', 'description', 'value_centre']
