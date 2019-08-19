""" Period serializers"""

from rest_framework import serializers

from src.api.models import Period

class PeriodSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ['name', 'start', 'end', 'period']
