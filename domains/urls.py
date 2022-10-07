from django.urls import path
from .views import DomainList, DomainDetail, MailServerList, MailServerDetail


urlpatterns = [
    path('domain/api/', DomainList.as_view()),
    path('domain/api/<int:pk>/', DomainDetail.as_view()),
    path('mailserver/api/', MailServerList.as_view()),
    path('mailserver/api/<int:pk>/', MailServerDetail.as_view()),
]
