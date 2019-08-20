""" Transactions serializers"""

from rest_framework import serializers

from src.api.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):

    revenue_stream = serializers.SerializerMethodField()

    def get_channel(self, obj):
        return obj.channel.name
    

    def get_revenue_stream(self, obj):
        return obj.revenue_stream.name

    class Meta:
        model = Transaction
        fields = ['revenue_stream', 'amount',]


