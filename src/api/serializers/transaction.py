""" Transactions serializers"""

from rest_framework import serializers

from src.api.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):

    income_stream = serializers.SerializerMethodField()

    def get_income_stream(self, obj):
        return obj.income_stream.name
    

    class Meta:
        model = Transaction
        fields = [ 'amount', 'income_stream']


