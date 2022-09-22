from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class HostingCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = HostingCompany
        fields = '__all__'


class AppPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppPlatform
        fields = '__all__'


class ServerSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Server
        fields = '__all__'

