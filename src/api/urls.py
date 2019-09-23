from django.urls import path
from .views import *

from .views.metric import MetricListCreateAPIView

urlpatterns = [
    path('company/', CompanyListCreateAPIView.as_view(), name='company'),
    path('period/', PeriodListAPIView.as_view(), name='period'),
    path('value_centre/<int:company_id>/', ValueCentreListCreateAPIView.as_view(), name='value_centre'),
    path(
        'value_centre/<int:company_id>/<str:period_type>/<str:year>/',
        ValueCentreListAPIView.as_view(),
        name='value_centre_list'),

    path(
        'product/<int:value_centre_id>/<str:period_type>/<str:year>/',
        ProductListAPIView.as_view(),
        name='product_list'),
    path('product/<int:value_centre_id>/', ProductCreateAPIView.as_view(), name='product'),
    path(
        'revenue_stream/<int:product_id>/<str:period_type>/<str:year>/',
        RevenueStreamListAPIView.as_view(),
        name='revenue_stream_list'
        ),
    path(
        'revenue_stream/<int:product_id>/',
        RevenueStreamCreateAPIView.as_view(),
        name='revenue_stream'
        ),
    path('transaction/<int:revenue_stream_id>/', TransactionListCreateAPIView.as_view(), name='transaction'),
    path('product_transactions/<int:product_id>/', ProductTransactionsList.as_view(), name='product_transactions'),
    path('company_revenue_streams/<int:company_id>/', CompanyRevenueStreams.as_view(), name='company_revenue_streams'),
    path('metric/', MetricListCreateAPIView.as_view(), name='metric'),    
    path(
        'income_stream/<int:revenue_stream_id>/<str:period_type>/<str:year>/',
        IncomeStreamListAPIView.as_view(),
        name='income_stream'
        ),
    path(
        'income_stream_target/<int:income_stream_id>/',
        IncomeStreamTargetListCreateAPIView.as_view(),
        name='income_stream_target'
        ),
    path(
        'value_centre_target/<int:value_centre_id>/',
        ValueCentreTargetListCreateAPIView.as_view(),
        name='value_centre_target'
        ),
    path(
        'product_target/<int:product_id>/',
        ProductTargettListCreateAPIView.as_view(),
        name='product_target'
        ),
    path(
        'revenue_stream_target/<int:revenue_stream_id>/',
        RevenueStreamTargetListCreateAPIView.as_view(),
        name='revenue_stream_target'
        ),
]
