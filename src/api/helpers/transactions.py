""" Transactions helpers"""
import os
import requests
import datetime
import math
from dateutil.relativedelta import relativedelta
from django.shortcuts import get_object_or_404

from src.api.models import Transaction, IncomeStream
from src.api.helpers.percentage import get_percentage


transactions_url = os.getenv('TRANSACTONS_URL')
cred = os.getenv('CRED')


def get_transactions(revenue_stream):
    """Get transactions from a third party api and populate our db"""
    format_transaction_url = transactions_url.format(revenue_stream.name.lower())
    try:
        response = requests.get(format_transaction_url,auth=(cred, cred)).json()['results']
    except Exception as err:
        print(err)
        return
    for res in response:
        for item in res['results']:
            transactions = item['items']
            income_stream, _ = IncomeStream.objects.get_or_create(
                name=item['revenue_stream'] or 'Noname',
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
    return

def get_all_months_and_quotas():
    """ Get all months in an year helper"""
    all_months = []
    all_quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    for i in range(1,13):
        all_months.append(datetime.date(2008, i, 1).strftime('%B'))
    return all_months, all_quarters

def get_all_days():
    all_days = []
    today = datetime.date.today()
    num_of_days = 7
    for i in range(1,8):
        start_day = today + datetime.timedelta(-num_of_days)
        all_days.append(start_day.strftime('%A'))
        num_of_days -= 1
    return all_days

def months_generator(year):
    """ Generate months"""
    result = []
    today = datetime.date.today()
    current = datetime.date(year, 1, 1)
    if today.year != current.year:
        today = datetime.date(year, 12, 31)
    while current <= today:
        result.append(current.strftime('%B'))
        current += relativedelta(months=1)
    return result

def quarter_generator(year):
    """ Generate quotas in an year"""
    months = months_generator(year)
    all_quotas = ['Q1', 'Q2', 'Q3', 'Q4']
    number_of_quotas = math.ceil(len(months)/3)
    quotas = all_quotas[:number_of_quotas]
    return quotas

class TransactionsFilterHelper():
    """ A general class to help filter tranactions
        for different end points
    """

    def get_past_week_transactions_data(transactions):
        """
        Get transactions data with past week filter
        """
        transactions_value = 0
        total_target = 0
        number_of_transactions = 0
        g_data = []
        days = get_all_days()
        num_of_days = 7
        for day in days:
            start_date = datetime.datetime.now() + datetime.timedelta(-num_of_days)
            value = 0
            day_date = start_date.strftime('%Y-%m-%d')[5:10]
            for t in transactions:
                transaction_date = t.date_paid[5:10]
                if transaction_date == day_date:
                    transactions_value += t.amount
                    number_of_transactions += 1
                    value += t.amount
            num_of_days = num_of_days - 1
            g_data_obj = {
                "value": round(value, 2),
                "label": day
            }
            g_data.append(g_data_obj)
        return (
            transactions_value,
            total_target,
            number_of_transactions,
            g_data
        )

    def get_past_month_transactions_data(transactions, targets):
        """
        Get transactions data with past month filter
        """
        transactions_value = 0
        total_target = 0
        number_of_transactions = 0
        g_data = []
        weeks = ['Week1', 'Week2', 'Week3', 'Week4']
        start_date = datetime.datetime.now() + datetime.timedelta(-30)
        for week in weeks:
            value = 0
            prev_week_end = start_date
            format_week_end = prev_week_end.strftime('%Y-%m-%d')
            current_week_end = (prev_week_end + datetime.timedelta(7)).strftime('%Y-%m-%d')
            for t in transactions:
                transaction_date = t.date_paid[:9]
                if transaction_date > format_week_end and transaction_date <= current_week_end:
                    transactions_value += t.amount
                    number_of_transactions += 1
                    value += t.amount
            g_data_obj = {
                "value": round(value, 2),
                "label": week
            }
            g_data.append(g_data_obj)
            for target in targets:
                end_date = datetime.datetime.now().strftime('%B').lower()
                start_date_month = start_date.strftime('%B')
                period_name = target.period.name.lower()
                if period_name == end_date or period_name == start_date_month.lower():
                    total_target += target.amount
        return (
            transactions_value,
            total_target,
            number_of_transactions,
            g_data
        )

    def get_quarterly_transactions_data(transactions, targets, year):
        """
        Get transactions data with quarterly filter
        """
        quarters = quarter_generator(year)
        _, all_quarters = get_all_months_and_quotas()
        transactions_value = 0
        total_target = 0
        number_of_transactions = 0
        g_data = []
        prev_month = 0
        for quarter in quarters:
            current_m = prev_month + 1 
            current_m1 = prev_month+ 2
            current_m2 = prev_month + 3
            prev_month = current_m2
            value = 0
            for t in transactions:
                transaction_month = int(t.date_paid[5:7])
                if current_m == transaction_month \
                    or current_m1 == transaction_month \
                        or current_m2 == transaction_month:
                    value += t.amount
                    transactions_value += t.amount
                    number_of_transactions += 1
            g_data_obj = {
                "value": round(value, 2),
                "label": quarter
            }
            g_data.append(g_data_obj)
        for q in all_quarters:
            for target in targets:
                if target.period.name.lower() == q.lower():
                    total_target += target.amount
        return (
            transactions_value,
            total_target,
            number_of_transactions,
            g_data
        )
    
    def get_monthly_transactions_data(transactions, targets, year):
        transactions_value = 0
        total_target = 0
        number_of_transactions = 0
        g_data = []
        months = months_generator(year)
        all_months, _ = get_all_months_and_quotas()
        for month in months:
            current_month = months.index(month) + 1
            value = 0
            for t in transactions:
                transaction_month = int(t.date_paid[5:7])
                if current_month == transaction_month:
                    value += t.amount
                    transactions_value += t.amount
                    number_of_transactions += 1
            g_data_obj = {
                "value": round(value, 2),
                "label": month
            }
            g_data.append(g_data_obj)
        for m in all_months:
            for target in targets:
                if target.period.name.lower() == m.lower():
                    total_target += target.amount
        return (
            transactions_value,
            total_target,
            number_of_transactions,
            g_data
        )
        
class IncomeStreamTransactionsFilter:

    def get_transactions_data(period_type, transactions, targets, year):
        if period_type == 'past_week':
            (
            transactions_value,
            total_target,
            number_of_transactions,
            g_data
            ) = TransactionsFilterHelper.get_past_week_transactions_data(transactions)
        if period_type == 'past_month':
            (
            transactions_value,
            total_target,
            number_of_transactions,
            g_data
            ) = TransactionsFilterHelper.get_past_month_transactions_data(
                transactions, targets
            )
        if period_type == 'quarterly':
            (
            transactions_value,
            total_target,
            number_of_transactions,
            g_data
            ) = TransactionsFilterHelper.get_quarterly_transactions_data(
                transactions, targets, year
            )
        if period_type == 'monthly':
            (
            transactions_value,
            total_target,
            number_of_transactions,
            g_data
            ) = TransactionsFilterHelper.get_monthly_transactions_data(
                transactions, targets, year
            )
        percentage = get_percentage(transactions_value, total_target)
        
        return (
            percentage,
            transactions_value,
            total_target,
            number_of_transactions,
            g_data
            )
