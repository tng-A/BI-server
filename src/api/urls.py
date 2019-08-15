from django.urls import path
from .views import *

from .views.metric import MetricListCreateAPIView
from .analytics import (
    IncomeStreamTrends,
    IncomeStreamCard
)

urlpatterns = [
    path('company/', CompanyListCreateAPIView.as_view(), name='company'),
    path('value_centre/<int:company_id>/', ValueCentreListCreateAPIView.as_view(), name='value_centre'),
    path('department/<int:value_centre_id>/', DepartmentListCreateAPIView.as_view(), name='department'),
    path('product/<int:department_id>/', ProductListCreateAPIView.as_view(), name='product'),
    path('revenue_type/<int:product_id>/', RevenueTypeListCreateAPIView.as_view(), name='revenue_type'),
    path(
        'revenue_stream/<int:revenue_type_id>/',
        RevenueStreamListCreateAPIView.as_view(),
        name='revenue_stream'
        ),
    path(
        'income_stream/<int:revenue_stream_id>/',
        IncomeStreamListCreateAPIView.as_view(),
        name='income_stream'
        ),
    path('metric/', MetricListCreateAPIView.as_view(), name='metric'),
    path(
        'value_centre_target/<int:value_centre_id>/',
        ValueCentreTargetListCreateAPIView.as_view(),
        name='value_centre_target'
        ),
    path(
        'department_target/<int:department_id>/',
        DepartmentTargetListCreateAPIView.as_view(),
        name='department_target'
        ),
    path(
        'product_target/<int:product_id>/',
        ProductTargettListCreateAPIView.as_view(),
        name='product_target'
        ),
    path(
        'revenue_type_target/<int:revenue_type_id>/',
        RevenueTypeTargetListCreateAPIView.as_view(),
        name='revenue_type_target'
        ),
    path(
        'revenue_stream_target/<int:revenue_stream_id>/',
        RevenueStreamTargetListCreateAPIView.as_view(),
        name='revenue_stream_target'
        ),
    path(
        'income_stream_target/<int:income_stream_id>/',
        IncomeStreamTargetListCreateAPIView.as_view(),
        name='income_stream_target'
        ),
    path(
        'value_centre_okr/<int:value_centre_id>/',
        ValueCentreOKRListCreateAPIView.as_view(),
        name='value_centre_okr'
        ),
    path(
        'product_okr/<int:product_id>/',
        ProductOKRListCreateAPIView.as_view(),
        name='product_okr'
        ),
    path(
        'income_stream_okr/<int:income_stream_id>/',
        IncomeStreamOKRListCreateAPIView.as_view(),
        name='income_stream_okr'
        ),
    path(
        'department_okr/<int:department_id>/',
        DepartmentOKRListCreateAPIView.as_view(),
        name='department_okr'
        ),
    path(
        'revenue_type_okr/<int:revenue_type_id>/',
        RevenueTypeOKRListCreateAPIView.as_view(),
        name='revenue_type_okr'
        ),
    path(
        'revenue_stream_okr/<int:revenue_stream_id>/',
        RevenueStreamOKRListCreateAPIView.as_view(),
        name='revenue_stream_okr'
        ),
    path(
        'income_stream_trends/<int:income_stream_id>/<str:start>/<str:end>',
        IncomeStreamTrends.as_view(),
        name='income_stream_trends'
        ),
    path(
        'income_stream_card/<int:income_stream_id>/<str:start>/<str:end>',
        IncomeStreamCard.as_view(),
        name='income_stream_card'
        ),
]
