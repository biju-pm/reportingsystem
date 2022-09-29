from rest_framework import generics

from .models import Domain
from .serializers import DomainSerializer


class DomainList(generics.ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class DomainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

    def perform_update(self, serializer):
        serializer.save()

