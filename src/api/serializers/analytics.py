""" Custom analytics serializers"""


from rest_framework import serializers


class IncomeStreamCardSerializer(serializers.Serializer):
    """ IncomeStreamCard  serializer"""

    target = serializers.FloatField()
    name = serializers.CharField()
    okr_value = serializers.FloatField()
    percentage = serializers.FloatField()
