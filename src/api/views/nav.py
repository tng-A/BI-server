""" Nav views"""

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from src.api.models import ValueCentre, Company, Product, RevenueStream, IncomeStream
from src.api.serializers.nav import NavSerializer
from src.api.helpers.check_resource import resource_exists


class NavItems(ListAPIView):
    serializer_class = NavSerializer
    queryset = ValueCentre.objects.all()

    def list(self, request, *args, **kwargs):
        company = resource_exists(Company, kwargs['company_id'])
        if not company:
            message = 'Company does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        value_centres = company.value_centres.all()
        for value_centre in value_centres:
            value_centre.visible_to =  ['company_users']           
            products = Product.objects.filter(
                value_centre=value_centre
            )
            for product in products:
                product.visible_to =  ['value_centre_users', 'company_users']              
                revenue_streams = RevenueStream.objects.filter(
                product=product
                )
                for revenue_stream in revenue_streams:
                    revenue_stream.visible_to = ['value_centre_users', 'company_users','product_users']              
                    income_streams = IncomeStream.objects.filter(
                        revenue_stream=revenue_stream
                    )
                    revenue_stream.income_stream = income_streams
                product.revenue_stream = revenue_streams
            value_centre.product = products
        serializer = self.get_serializer(value_centres, many=True)
        return Response(serializer.data)
        
