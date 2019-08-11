""" ValueCentre views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.value_centre import ValueCentreSerializer
from src.api.models import Subsidiary
from src.api.models import ValueCentre


class ValueCentreListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ValueCentreSerializer
    queryset = ValueCentre.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            subsidiary = Subsidiary.objects.get(pk=self.kwargs['subsidiary_id'])
        except Subsidiary.DoesNotExist:
            message = 'Subsidiary does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = subsidiary.value_centres.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            subsidiary = Subsidiary.objects.get(pk=self.kwargs['subsidiary_id'])
        except Subsidiary.DoesNotExist:
            message = 'Subsidiary does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        exists = ValueCentre.objects.all().filter(
            name__icontains=data['name'],
            description__icontains=data['description'],
            subsidiary__country__iexact=subsidiary.country,
            subsidiary__town__iexact=subsidiary.town
        )
        if len(exists) > 0:
            message = 'That value centre already exists'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer_context = {
            'request': request,
            'subsidiary': subsidiary
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(subsidiary=subsidiary)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
