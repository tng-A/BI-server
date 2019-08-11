""" Subsidiary serializers"""

from rest_framework import serializers

from src.api.models.subsidiary import Subsidiary


class SubsidiarySerializer(serializers.ModelSerializer):
    """ Subsidiary model serializer"""

    company = serializers.SerializerMethodField()

    def get_company(self,obj):
        return obj.company.name

    class Meta:
        """ Meta options"""
        
        model = Subsidiary
        fields = ['country', 'town', 'company']
