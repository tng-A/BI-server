""" Company serializers"""

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from src.api.models.company import Company


class CompanySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(
            queryset=Company.everything.all(),
            message='The company name already exists. Kindly try another.'
        )]
    )

    class Meta:
        model = Company
        fields = ['name', 'description']
