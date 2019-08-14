""" Product views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.product import ProductSerializer
from src.api.models import Product
from src.api.models import Department


class ProductListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            department = Department.objects.get(pk=self.kwargs['department_id'])
        except Department.DoesNotExist:
            message = 'Department does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = department.products.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            department = Department.objects.get(pk=self.kwargs['department_id'])
        except Department.DoesNotExist:
            message = 'Department does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        exists = Product.objects.all().filter(
            name__icontains=data['name'],
            department__name__iexact=department.name
        )
        if len(exists) > 0:
            message = 'That product already exists'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer_context = {
            'request': request,
            'department': department
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(department=department)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
