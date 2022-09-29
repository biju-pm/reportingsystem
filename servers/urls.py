from django.urls import path
from .views import ServerList, ServerDetail

urlpatterns = [
    path('servers/api/', ServerList.as_view()),
    path('servers/api/<int:pk>/', ServerDetail.as_view()),
    # path('dns/api/', DnsRecordList.as_view()),
    # path('dns/api/<int:pk>/', DnsRecordDetail.as_view()),
    # path('dnsdetails/api/', DnsDetailsList.as_view()),
    # path('dnsdetails/api/<int:pk>/', DnsDetailsDetail.as_view()),
]
