""" Product views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.product import ProductSerializer
from src.api.models import Product
from src.api.models import ValueCentre


class ProductListCreateAPIView(ListCreateAPIView):
    """ List/Create products"""
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            value_centre = ValueCentre.objects.get(pk=kwargs['value_centre_id'])
        except ValueCentre.DoesNotExist:
            message = 'ValueCentre does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = value_centre.products.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            value_centre = ValueCentre.objects.get(pk=kwargs['value_centre_id'])
        except ValueCentre.DoesNotExist:
            message = 'ValueCentre does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        exists = Product.objects.all().filter(
            name__icontains=data['name'],
            value_centre__name__iexact=value_centre.name
        )
        if len(exists) > 0:
            message = 'That product already exists'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer_context = {
            'request': request,
            'value_centre': value_centre
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(value_centre=value_centre)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
