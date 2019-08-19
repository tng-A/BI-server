""" Income Stream Analysis file"""

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

from src.api.models import IncomeStreamOKR, IncomeStream
from src.api.serializers.analytics import IncomeStreamCardSerializer
from src.api.serializers.okr import IncomeStreamOKRSerializer
from src.api.helpers.analytics_helper import income_stream_okr

class IncomeStreamTrends(generics.ListAPIView):
    """
    Income trends in monthly basis
    """
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = IncomeStreamOKRSerializer
    queryset = IncomeStreamOKR.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            income_stream = IncomeStream.objects.get(pk=kwargs['income_stream_id'])
        except IncomeStream.DoesNotExist:
            message = 'IncomeStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = income_stream.okrs.all()
        filtered_okr = income_stream_okr(queryset, *args, **kwargs)
        serializer = self.get_serializer(filtered_okr, many=True)
        return Response(serializer.data)

class IncomeStreamCard(generics.ListAPIView):
    """
    Income streams card data
    Return:
        target, income_stream_name, total_okr_value, total_okr_value/target * 100(percentage)
    """
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = IncomeStreamCardSerializer
    queryset = IncomeStreamOKR.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            income_stream = IncomeStream.objects.get(pk=kwargs['income_stream_id'])
        except IncomeStream.DoesNotExist:
            message = 'IncomeStream does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        income_stream_name = income_stream.name
        target = income_stream.targets.all()[0].amount
        okrs = income_stream.okrs.all()
        filtered_okr = income_stream_okr(okrs, *args, **kwargs)
        total_okr_value = 0
        for okr in filtered_okr:
            total_okr_value += okr.amount
        percentage = total_okr_value/target * 100
        qs=[]
        data = {
            "target": target,
            "name": income_stream_name,
            "okr_value": total_okr_value,
            "percentage": percentage
        }
        qs.append(data)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
