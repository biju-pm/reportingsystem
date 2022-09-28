from rest_framework import generics

from .models import Vendor, VendorCategory, ApiKeys
from .serializers import VendorSerializer, VendorCategorySerializer, ApiKeysSerializer


class VendorCategoryList(generics.ListCreateAPIView):
    queryset = VendorCategory.objects.all()
    serializer_class = VendorCategorySerializer


class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def perform_update(self, serializer):
        serializer.save()


class ApiKeysList(generics.ListCreateAPIView):
    queryset = ApiKeys.objects.all()
    serializer_class = ApiKeysSerializer

    def perform_create(self, serializer):
        serializer.save()


class ApiKeysDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApiKeys.objects.all()
    serializer_class = ApiKeysSerializer

    def perform_update(self, serializer):
        serializer.save()
