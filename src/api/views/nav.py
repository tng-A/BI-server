""" Nav views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import TokenAuthentication

from src.api.models import ValueCentre, Company, Product, RevenueStream, IncomeStream
from src.api.serializers.nav import NavSerializer

class NavItems(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication,)
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
            value_centre.visible_to =  ['company_users']           
            products = Product.objects.filter(
                value_centre=value_centre
            )
            for product in products:
                product.visible_to =  ['value_centre_users']              
                revenue_streams = RevenueStream.objects.filter(
                product=product
                )
                for revenue_stream in revenue_streams:
                    revenue_stream.visible_to = ['product_users']              
                    income_streams = IncomeStream.objects.filter(
                        revenue_stream=revenue_stream
                    )
                    revenue_stream.income_stream = income_streams
                product.revenue_stream = revenue_streams
            value_centre.product = products
        serializer = self.get_serializer(value_centres, many=True)
        return Response(serializer.data)
        
