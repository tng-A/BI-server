""" Metric serializers"""

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from src.api.models.metric import Metric


class MetricSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(
            queryset=Metric.everything.all(),
            message='The metric name already exists. Kindly try another.'
        )]
    )

    class Meta:
        model = Metric
        fields = ['name',]
