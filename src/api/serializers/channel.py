""" Channel serializers"""

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from src.api.models.channel import Channel


class ChannelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(
            queryset=Channel.everything.all(),
            message='The channel name already exists. Kindly try another.'
        )]
    )

    class Meta:
        model = Channel
        fields = ['name']
