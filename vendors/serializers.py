from rest_framework import serializers

from .models import Vendor, VendorCategory, ApiKeys


class VendorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorCategory
        fields = ['id', 'name']


class VendorSerializer(serializers.ModelSerializer):
    category = VendorCategorySerializer(many=False)

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'description', 'image', 'category']


class ApiKeysSerializer(serializers.ModelSerializer):
    vendor = serializers.PrimaryKeyRelatedField(queryset=Vendor.objects.all())

    class Meta:
        model = ApiKeys
        fields = ['id', 'vendor', 'api_key', 'api_secret']

