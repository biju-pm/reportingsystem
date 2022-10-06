from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet, ClientDetail, TicketDetailView,\
    ClientList, ClientCreateView, TicketListView, ClientStaffView

# router = routers.DefaultRouter()
# router.register(r'clients', ClientViewSet)
# router.register(r'users', UserViewSet)

urlpatterns = [
    # path('api/', include(router.urls)),
    # path('client/', ClientView.as_view()),
    path('client/<int:pk>/', ClientDetail.as_view()),
    path('client/list/api/', ClientList.as_view()),
    path('client/create/', ClientCreateView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('ticket/api/', TicketListView.as_view()),
    path('ticket/api/<int:pk>/', TicketDetailView.as_view()),
    path('client/staff/api/', ClientStaffView.as_view()),
]
