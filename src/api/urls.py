from django.urls import path
from .views import *

from .views.metric import MetricListCreateAPIView
from .views.target import (
    ValueCentreTargetListCreateAPIView,
    ProductTargettListCreateAPIView,
    IncomeStreamTargetListCreateAPIView
)
from .views.okr import (
    ValueCentreOKRListCreateAPIView,
    ProductOKRListCreateAPIView,
    IncomeStreamOKRListCreateAPIView
)
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
    path('revenue_stream/<int:revenue_type_id>/', RevenueStreamListCreateAPIView.as_view(), name='revenue_stream'),
    path('income_stream/<int:revenue_stream_id>/', IncomeStreamListCreateAPIView.as_view(), name='income_stream'),
    path('metric/', MetricListCreateAPIView.as_view(), name='metric'),
    path('value_centre_target/<int:value_centre_id>/', ValueCentreTargetListCreateAPIView.as_view(), name='v_c_target'),
    path('product_target/<int:product_id>/', ProductTargettListCreateAPIView.as_view(), name='product_target'),
    path('income_stream_target/<int:income_stream_id>/', IncomeStreamTargetListCreateAPIView.as_view(), name='income_stream_target'),
    path('value_centre_okr/<int:value_centre_id>/', ValueCentreOKRListCreateAPIView.as_view(), name='v_c_okr'),
    path('product_okr/<int:product_id>/', ProductOKRListCreateAPIView.as_view(), name='product_okr'),
    path('income_stream_okr/<int:income_stream_id>/', IncomeStreamOKRListCreateAPIView.as_view(), name='income_stream_okr'),
    path(
        'income_stream_trends/<int:income_stream_id>/<str:start>/<str:end>',
        IncomeStreamTrends.as_view(),
        name='income_stream_trends'),
    path(
        'income_stream_card/<int:income_stream_id>/<str:start>/<str:end>',
        IncomeStreamCard.as_view(),
        name='income_stream_card'),
]
