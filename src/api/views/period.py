""" Period view"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.period import PeriodSerializer
from src.api.models.period import Period

class PeriodListAPIView(ListAPIView):
    """ List/Create period"""
    permission_classes =(IsAuthenticated,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()
