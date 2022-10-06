from django.urls import path
from .views import ServerList, ServerDetail, ServerCreate, ServerUpdate

urlpatterns = [
    path('servers/api/', ServerList.as_view()),
    path('servers/api/<int:pk>/', ServerDetail.as_view()),
    path('servers/api/create/', ServerCreate.as_view()),
    path('servers/api/update/<int:pk>/', ServerUpdate.as_view()),
]
