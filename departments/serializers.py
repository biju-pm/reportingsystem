from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def create(self, validated_data):
        return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        department = super().update(instance, validated_data)
        return department


