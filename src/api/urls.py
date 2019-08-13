from django.urls import path
from .views.company import CompanyListCreateAPIView
from .views.subsidiary import SubsidiaryListCreateAPIView
from .views.value_centre import ValueCentreListCreateAPIView
from .views.product import ProductListCreateAPIView
from .views.income_stream import (
    IncomeStreamListCreateAPIView
)
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
    path('subsidiary/<int:company_id>/', SubsidiaryListCreateAPIView.as_view(), name='subsidiary'),
    path('value_centre/<int:subsidiary_id>/', ValueCentreListCreateAPIView.as_view(), name='value_centre'),
    path('product/<int:value_centre_id>/', ProductListCreateAPIView.as_view(), name='product'),
    path('income_stream/<int:product_id>/', IncomeStreamListCreateAPIView.as_view(), name='income_stream'),
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
