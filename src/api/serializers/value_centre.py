""" ValueCentre serializers"""

from rest_framework import serializers

from src.api.models.value_centre import ValueCentre
from src.api.serializers.company import CompanySerializer
from src.api.serializers.okr import ValueCentreOKRSerializer
from src.api.serializers.target import ValueCentreTargetSerializer


class ValueCentreSerializer(serializers.ModelSerializer):
    """ ValueCentre model serializer"""
    company = CompanySerializer(read_only=True)
    total_target = serializers.FloatField()
    total_okr = serializers.FloatField()
    objective_key_results = ValueCentreOKRSerializer(many=True)
    value_centre_targets = ValueCentreTargetSerializer(many=True)
    percentage = serializers.FloatField()


    class Meta:
        """ Meta options"""
        
        model = ValueCentre
        fields = [ 'id', 'name', 'total_target',
                    'total_okr', 'percentage', 'value_centre_targets',
                    'objective_key_results', 'company']
