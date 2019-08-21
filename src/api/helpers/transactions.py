""" Transactions helpers"""

import requests
import datetime
from dateutil.relativedelta import relativedelta
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
                name=item['revenue_stream'],
                revenue_stream=revenue_stream)
            for transaction in transactions:
                try:
                    Transaction.objects.create(
                    date_paid=transaction['date_paid'],
                    receipt_number=transaction['receipt_number'],
                    amount=transaction['amount_paid'],
                    income_stream=income_stream
                    )
                except:
                    continue   
    return Transaction.objects.all()

def months_generator(year):
    result = []
    today = datetime.date.today()
    current = datetime.date(year, 1, 1)
    if today.year != current.year:
        today = datetime.date(year, 12, 31)
    while current <= today:
        result.append(current.strftime('%B'))
        current += relativedelta(months=1)
    return result
    

