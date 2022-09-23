from django.urls import path
from .views import VendorList, VendorDetail

urlpatterns = [
    path('vendors/api/', VendorList.as_view(), name='vendors'),
    path('vendors/api/<int:pk>/', VendorDetail.as_view(), name='vendor-detail'),
]