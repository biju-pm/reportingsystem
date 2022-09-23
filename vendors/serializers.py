from rest_framework import serializers

from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'description', 'public_key', 'private_key', 'image']
