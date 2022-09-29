from django.urls import path
from .views import DomainList, DomainDetail


urlpatterns = [
    path('domain/api/', DomainList.as_view()),
    path('domain/api/<int:pk>/', DomainDetail.as_view()),
]
