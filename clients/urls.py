from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet, ClientDetail, \
    ClientList, ClientCreateView, TicketSerializerView, ClientStaffView

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
    path('ticket/api/', TicketSerializerView.as_view()),
    path('client/staff/api/', ClientStaffView.as_view()),
]
