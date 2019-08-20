""" Transactions helpers"""

import requests
from django.shortcuts import get_object_or_404

from src.api.models import Transaction, IncomeStream

def get_transactions(revenue_stream):
    prev_trans = 0    
    response = requests.get(
        'http://embu.jambopay.co.ke:8080/api/v1/aggregate_report/?z=true`',
        auth=('admin', 'admin')
        ).json()
    for res in response['results']:
        for item in res['results']:
            transactions = item['items']
            income_stream, _ = IncomeStream.objects.get_or_create(
                name=item['revenue_stream'])
            for transaction in transactions:
                try:
                    Transaction.objects.create(
                    date_paid=transaction['date_paid'],
                    receipt_number=transaction['receipt_number'],
                    amount=transaction['amount_paid'],
                    revenue_stream=revenue_stream,
                    income_stream=income_stream
                    )
                except:
                    continue   
    return Transaction.objects.all()

def get_new_transactions():
    prev_trans = 0
    actual_request = requests.get(
        'http://embu.jambopay.co.ke:8080/api/v1/aggregate_report/?z=true`',
        auth=('admin', 'admin')
        )
    return actual_request

