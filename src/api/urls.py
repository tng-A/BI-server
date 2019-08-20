from django.urls import path
from .views import *

from .views.metric import MetricListCreateAPIView
from .analytics import (
    IncomeStreamTrends,
    IncomeStreamCard
)

urlpatterns = [
    path('company/', CompanyListCreateAPIView.as_view(), name='company'),
    path('channel/', ChannelListCreateAPIView.as_view(), name='channel'),
    path('value_centre/<int:company_id>/', ValueCentreListCreateAPIView.as_view(), name='value_centre'),
    path('product/<int:value_centre_id>/', ProductListCreateAPIView.as_view(), name='product'),
    path(
        'revenue_stream/<int:product_id>/',
        RevenueStreamListCreateAPIView.as_view(),
        name='revenue_stream'
        ),
    path('transaction/<int:revenue_stream_id>/', TransactionListCreateAPIView.as_view(), name='transaction'),
    path('product_transactions/<int:product_id>/', ProductTransactionsList.as_view(), name='product_transactions'),
    path('company_revenue_streams/<int:company_id>/', CompanyRevenueStreams.as_view(), name='company_revenue_streams'),
    path('metric/', MetricListCreateAPIView.as_view(), name='metric'),    
    # path(
    #     'income_stream/<int:revenue_stream_id>/',
    #     IncomeStreamListCreateAPIView.as_view(),
    #     name='income_stream'
    #     ),
    # path(
    #     'value_centre_target/<int:value_centre_id>/',
    #     ValueCentreTargetListCreateAPIView.as_view(),
    #     name='value_centre_target'
    #     ),
    # path(
    #     'product_target/<int:product_id>/',
    #     ProductTargettListCreateAPIView.as_view(),
    #     name='product_target'
    #     ),
    # path(
    #     'revenue_stream_target/<int:revenue_stream_id>/',
    #     RevenueStreamTargetListCreateAPIView.as_view(),
    #     name='revenue_stream_target'
    #     ),
    # path(
    #     'income_stream_target/<int:income_stream_id>/',
    #     IncomeStreamTargetListCreateAPIView.as_view(),
    #     name='income_stream_target'
    #     ),
    # path(
    #     'value_centre_okr/<int:value_centre_id>/',
    #     ValueCentreOKRListCreateAPIView.as_view(),
    #     name='value_centre_okr'
    #     ),
    # path(
    #     'filtered_value_centres_okrs/<int:company_id>/<str:period_type>/<str:year>',
    #     FilteredValueCentresOKRSListAPIView.as_view(),
    #     name='filtered_value_centres_okrs'
    #     ),
    # path(
    #     'product_okr/<int:product_id>/',
    #     ProductOKRListCreateAPIView.as_view(),
    #     name='product_okr'
    #     ),
    # path(
    #     'income_stream_okr/<int:income_stream_id>/',
    #     IncomeStreamOKRListCreateAPIView.as_view(),
    #     name='income_stream_okr'
    #     ),
    # path(
    #     'revenue_stream_okr/<int:revenue_stream_id>/',
    #     RevenueStreamOKRListCreateAPIView.as_view(),
    #     name='revenue_stream_okr'
    #     ),
    # path(
    #     'income_stream_trends/<int:income_stream_id>/<str:start>/<str:end>',
    #     IncomeStreamTrends.as_view(),
    #     name='income_stream_trends'
    #     ),
    # path(
    #     'income_stream_card/<int:income_stream_id>/<str:start>/<str:end>',
    #     IncomeStreamCard.as_view(),
    #     name='income_stream_card'
    #     ),
]
