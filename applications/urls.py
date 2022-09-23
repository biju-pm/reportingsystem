from django.urls import path

from .views import ApplicationList, ApplicationDetail

urlpatterns = [
    path('applications/api/', ApplicationList.as_view()),
    path('applications/api/<int:pk>/', ApplicationDetail.as_view()),
]