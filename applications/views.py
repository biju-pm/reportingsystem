from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Application
from .serializers import ApplicationSerializer


class ApplicationList(ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
