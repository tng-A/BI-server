from django.urls import path
from .views.company import CompanyListCreateAPIView

urlpatterns = [
    path('company/', CompanyListCreateAPIView.as_view(), name='company'),
]
