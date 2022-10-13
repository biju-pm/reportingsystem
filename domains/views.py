from rest_framework import generics

from .models import Domain, MailServer
from .serializers import DomainSerializer, MailServerSerializer


class DomainList(generics.ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class DomainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class MailServerList(generics.ListCreateAPIView):
    queryset = MailServer.objects.all()
    serializer_class = MailServerSerializer


class MailServerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MailServer.objects.all()
    serializer_class = MailServerSerializer

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
