from rest_framework import serializers
from .models import Domain
from applications.models import Application
from vendors.models import Vendor


class DomainSerializer(serializers.ModelSerializer):
    application = serializers.SlugRelatedField(queryset=Application.objects.all(), slug_field='name')
    provider = serializers.SlugRelatedField(queryset=Vendor.objects.all(), slug_field='name')

    class Meta:
        model = Domain
        fields = ['id', 'name', 'is_purchased', 'first_optional_name', 'second_optional_name', 'application',
                  'is_active', 'provider']
