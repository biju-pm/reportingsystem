from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'client', 'ticket_number', 'ticket_status', 'ticket_type',
                  'description', 'ticket_priority', 'ticket_assigned_to', 'ticket_created_by',
                  'ticket_updated_by', 'created_at', 'updated_at')
        extra_kwargs = {'ticket_created_by': {'read_only': True}, 'ticket_updated_by': {'read_only': True},
                        'ticket_created_at': {'read_only': True}, 'ticket_updated_at': {'read_only': True}}

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

    def update(self, instance, validated_data):
        ticket = super().update(instance, validated_data)
        return ticket


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientStaff
        fields = '__all__'
