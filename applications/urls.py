from django.urls import path

from .views import ApplicationList, ApplicationDetail

urlpatterns = [
    path('application/api/', ApplicationList.as_view()),
    path('application/api/<int:pk>/', ApplicationDetail.as_view()),
]