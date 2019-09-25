""" Metric views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.metric import MetricSerializer
from src.api.models import Metric
from src.api.models import Company

class MetricListCreateAPIView(ListCreateAPIView):
    """ List/Create metrics"""
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = MetricSerializer
    queryset = Metric.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            company = Company.objects.get(pk=kwargs['company_id'])
        except Company.DoesNotExist:
            message = 'Company does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        metrics = company.metrics.all()
        serializer = self.get_serializer(metrics, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        try:
            company = Company.objects.get(pk=kwargs['company_id'])
        except Company.DoesNotExist:
            message = 'Company does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        serializer_context = {
            'request': request,
            'company': company
        }
        data = request.data
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(company=company)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
