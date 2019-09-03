""" Period serializers"""

from rest_framework import serializers

from src.api.models import Period

class PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period
        fields = ['name', 'year', 'period_type']
