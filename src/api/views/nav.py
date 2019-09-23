""" Nav views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from src.api.models import ValueCentre, Company, Product, RevenueStream, IncomeStream
from src.api.serializers.nav import NavSerializer

class NavItems(ListAPIView):
    permission_classes =(IsAuthenticated,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = NavSerializer
    queryset = ValueCentre.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            company = Company.objects.get(pk=kwargs['company_id'])
        except Company.DoesNotExist:
            message = 'Company does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        value_centres = company.value_centres.all()
        for value_centre in value_centres:
            products = Product.objects.filter(
                value_centre=value_centre
            )
            for product in products:
                revenue_streams = RevenueStream.objects.filter(
                product=product
                )
                for revenue_stream in revenue_streams:
                    income_streams = IncomeStream.objects.filter(
                        revenue_stream=revenue_stream
                    )
                    revenue_stream.income_stream = income_streams
                product.revenue_stream = revenue_streams                
            value_centre.product = products            
        serializer = self.get_serializer(value_centres, many=True)
        return Response(serializer.data)
        
