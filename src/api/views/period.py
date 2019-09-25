""" Period view"""

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.period import PeriodSerializer
from src.api.models import Period, Company
from src.api.helpers.check_resource import resource_exists


class PeriodListAPIView(ListAPIView):
    """ List/Create period"""
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()

    def list(self, request, *args, **kwargs):
        company = resource_exists(Company, kwargs['company_id'])
        if not company:
            message = 'Company does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        periods = company.periods.all()
        serializer = self.get_serializer(periods, many=True)
        return Response(serializer.data)
