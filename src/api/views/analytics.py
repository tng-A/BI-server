""" Analysis file"""

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

from src.api.models import IncomeStreamOKR, IncomeStream
from src.api.serializers.okr import IncomeStreamOKRSerializer


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
        start = kwargs.get('start', None)
        end = kwargs.get('end', None)
        filtered_okr = []
        for okr in queryset:
            if okr.period >= start and okr.period <= end:
                filtered_okr.append(okr)
        serializer = self.get_serializer(filtered_okr, many=True)
        return Response(serializer.data)
