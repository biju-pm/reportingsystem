from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Server
from .serializers import ServerSerializer


class ServerList(ListCreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
