from django.urls import path
from .views import ServerList, ServerDetail

urlpatterns = [
    path('servers/api/', ServerList.as_view()),
    path('servers/api/<int:pk>/', ServerDetail.as_view()),
]
