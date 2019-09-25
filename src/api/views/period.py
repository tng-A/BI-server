""" Period view"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.period import PeriodSerializer
from src.api.models import Period, Company

class PeriodListAPIView(ListAPIView):
    """ List/Create period"""
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            company = Company.objects.get(pk=kwargs['company_id'])
        except Company.DoesNotExist:
            message = 'Company does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        periods = company.periods.all()
        serializer = self.get_serializer(periods, many=True)
        return Response(serializer.data)
