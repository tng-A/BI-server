""" Metric views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.metric import MetricSerializer
from src.api.models import Metric
from src.api.models import Company

class MetricListCreateAPIView(ListCreateAPIView):
    """ List/Create metrics"""
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = MetricSerializer
    queryset = Metric.objects.all()
