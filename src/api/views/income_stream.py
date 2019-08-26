""" IncomeStream views"""

import datetime

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.income_stream import IncomeStreamSerializer
from src.api.helpers.transactions import (
    get_transactions,
    months_generator,
    quarter_generator,
    get_all_months_and_quotas
)
from src.api.models import (
    IncomeStream,
    RevenueStream
)


class IncomeStreamListAPIView(ListAPIView):
    """ Get all incomestreams (eg Parking) in a revenue stream(eg Embu) and transactions info"""
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = IncomeStreamSerializer
    queryset = IncomeStream.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            revenue_stream = RevenueStream.objects.get(pk=kwargs['revenue_stream_id'])
        except RevenueStream.DoesNotExist:
            message = 'RevenueStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        get_transactions(revenue_stream)
        income_streams = revenue_stream.income_streams.all()
        period_type = kwargs['period_type'].lower()
        year = int(kwargs['year'])
        quarters = quarter_generator(year)
        months = months_generator(year)
        all_months, all_quarters = get_all_months_and_quotas()
        for income_stream in income_streams:
            transactions_value = 0
            total_target = 0
            number_of_transactions = 0
            transactions = income_stream.transactions.filter(
                date_paid__contains=kwargs['year'])
            income_stream.transactions.set(transactions)
            targets = income_stream.targets.filter(
                period__period_type__icontains=period_type,
                period__year__contains=kwargs['year']
            )
            for transaction in transactions:
                transactions_value += transaction.amount
                number_of_transactions += 1
            g_data = []
            if len(transactions) > 0 or len(targets) > 0:
                if period_type == 'past_month':
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
                                value += t.amount
                        g_data_obj = {
                            "value": round(value, 2),
                            "label": week
                        }
                        g_data.append(g_data_obj)
                    targets = income_stream.targets.filter(period__year__contains=kwargs['year'])
                    for target in targets:
                        end_date = datetime.datetime.now().strftime('%B').lower()
                        start_date_month = start_date.strftime('%B')
                        period_name = target.period.name.lower()
                        if period_name == end_date or period_name == start_date_month.lower():
                            total_target += target.amount
                    
                if period_type == 'quarterly':
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
                        g_data_obj = {
                            "value": round(value, 2),
                            "label": quarter
                        }
                        g_data.append(g_data_obj)
                    for q in all_quarters:
                        for target in targets:
                            if target.period.name.lower() == q.lower():
                                total_target += target.amount
                if period_type == 'monthly':
                    for month in months:
                        current_month = months.index(month) + 1
                        value = 0
                        for t in transactions:
                            transaction_month = int(t.date_paid[5:7])
                            if current_month == transaction_month:
                                value += t.amount
                        g_data_obj = {
                            "value": round(value, 2),
                            "label": month
                        }
                        g_data.append(g_data_obj)
                    for m in all_months:
                        for target in targets:
                            if target.period.name.lower() == m.lower():
                                total_target += target.amount
            try:
                percentage = round((transactions_value / total_target) * 100, 2)
            except ZeroDivisionError:
                percentage = 0
            income_stream.transactions_value = transactions_value
            income_stream.number_of_transactions = number_of_transactions
            income_stream.total_target = total_target
            income_stream.achievement_percentage = percentage
            income_stream.graph_data = g_data
        serializer = self.get_serializer(income_streams, many=True)
        return Response(serializer.data)
