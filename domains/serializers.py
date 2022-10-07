from rest_framework import serializers
from .models import Domain, MailServer
from vendors.models import Vendor


class DomainSerializer(serializers.ModelSerializer):
    provider = serializers.SlugRelatedField(queryset=Vendor.objects.all(), slug_field='name')

    class Meta:
        model = Domain
        fields = ['id', 'name', 'is_purchased', 'first_optional_name', 'second_optional_name', 'is_active', 'provider']


class MailServerSerializer(serializers.ModelSerializer):
    provider = serializers.SlugRelatedField(queryset=Vendor.objects.all(), slug_field='name')

    class Meta:
        model = MailServer
        fields = ['id', 'name', 'is_purchased', 'is_active', 'provider']
