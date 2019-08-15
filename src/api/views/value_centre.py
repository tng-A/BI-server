""" ValueCentre views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.value_centre import ValueCentreSerializer
from src.api.models import (
    ValueCentre,
    Company
)


class ValueCentreListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = ValueCentreSerializer
    queryset = ValueCentre.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            company = Company.objects.get(pk=kwargs['company_id'])
        except Company.DoesNotExist:
            message = 'Company does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = company.value_centres.all()
        value_centres = []
        for v_c in queryset:
            total_target = 0
            total_okr = 0
            okr = []
            target = []
            value_centre = ValueCentre.objects.get(pk=v_c.id)
            targets = value_centre.targets.all()
            target += targets
            for t in targets:
                total_target += t.amount
            okrs = value_centre.okrs.all()
            for okr_var in okrs:
                total_okr += okr_var.amount
            okr += okrs
            try:
                percentage = (total_okr / total_target) * 100
            except ZeroDivisionError:
                percentage = 0
            v_c.objective_key_results = okr
            v_c.value_centre_targets = target
            v_c.percentage = percentage
            v_c.total_target = total_okr
            v_c.total_okr = total_okr
            value_centres.append(v_c)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            company = Company.objects.get(pk=kwargs['company_id'])
        except Company.DoesNotExist:
            message = 'Company does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        exists = ValueCentre.objects.all().filter(
            name__icontains=data['name'],
            company__name__iexact=company.name
        )
        if len(exists) > 0:
            message = 'That value centre already exists'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer_context = {
            'request': request,
            'company': company
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(company=company)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
