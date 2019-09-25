""" Company views"""

from rest_framework.generics import ListCreateAPIView

from src.api.serializers.company import CompanySerializer
from src.api.models import Company

class CompanyListCreateAPIView(ListCreateAPIView):
    """ List/Create companies"""
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
