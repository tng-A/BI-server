from django.urls import path
from .views.company import CompanyListCreateAPIView
from .views.subsidiary import SubsidiaryListCreateAPIView
from .views.value_centre import ValueCentreListCreateAPIView
from .views.product import ProductListCreateAPIView
from .views.income_stream import IncomeStreamListCreateAPIView
from .views.metric import MetricListCreateAPIView
from .views.target import (
    ValueCentreTargetListCreateAPIView,
    ProductTargettListCreateAPIView,
    IncomeStreamTargetListCreateAPIView
)


urlpatterns = [
    path('company/', CompanyListCreateAPIView.as_view(), name='company'),
    path('subsidiary/<int:company_id>/', SubsidiaryListCreateAPIView.as_view(), name='subsidiary'),
    path('value_centre/<int:subsidiary_id>/', ValueCentreListCreateAPIView.as_view(), name='value_centre'),
    path('product/<int:value_centre_id>/', ProductListCreateAPIView.as_view(), name='product'),
    path('income_stream/<int:product_id>/', IncomeStreamListCreateAPIView.as_view(), name='income_stream'),
    path('metric/', MetricListCreateAPIView.as_view(), name='metric'),
    path('v_c_target/<int:value_centre_id>/', ValueCentreTargetListCreateAPIView.as_view(), name='v_c_target'),
    path('product_target/<int:product_id>/', ProductTargettListCreateAPIView.as_view(), name='product_target'),
    path('income_stream_target/<int:income_stream_id>/', IncomeStreamTargetListCreateAPIView.as_view(), name='income_stream_target'),
]
