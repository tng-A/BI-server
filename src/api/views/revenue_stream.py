""" RevenueStream views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.revenue_stream import RevenueStreamSerializer
from src.api.models import (
    RevenueStream,
    RevenueType
)


class RevenueStreamListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = RevenueStreamSerializer
    queryset = RevenueStream.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            revenue_type = RevenueType.objects.get(pk=self.kwargs['revenue_type_id'])
        except RevenueType.DoesNotExist:
            message = 'RevenueType does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = revenue_type.revenue_streams.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            revenue_type = RevenueType.objects.get(pk=self.kwargs['revenue_type_id'])
        except RevenueType.DoesNotExist:
            message = 'RevenueType does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        exists = RevenueStream.objects.all().filter(
            name__icontains=data['name'],
            revenue_type__name__iexact=revenue_type.name
        )
        if len(exists) > 0:
            message = 'That revenue stream already exists'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer_context = {
            'request': request,
            'revenue_type': revenue_type
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(revenue_type=revenue_type)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
