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
    ticket_assigned_to = serializers.StringRelatedField(many=True)
    ticket_created_by = serializers.StringRelatedField(many=False)
    ticket_updated_by = serializers.StringRelatedField(many=False)

    class Meta:
        model = Ticket
        fields = ('id', 'client', 'ticket_number', 'ticket_status', 'ticket_type',
                  'description', 'ticket_priority', 'ticket_assigned_to', 'ticket_created_by',
                  'ticket_updated_by', 'created_at', 'updated_at', 'time_taken', 'ticket_due_date')
        extra_kwargs = {'ticket_created_by': {'read_only': True}, 'ticket_updated_by': {'read_only': True},
                        'ticket_created_at': {'read_only': True}, 'ticket_updated_at': {'read_only': True}}

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

    def update(self, instance, validated_data):
        ticket = super().update(instance, validated_data)
        return ticket

    def get_time_taken(self, obj):
        return obj.time_taken()


class ClientSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField(many=True)
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Client
        fields =['id', 'user', 'department', 'name', 'phone', 'address', 'city', 'state', 'zipcode']


class ClientStaffSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField(many=False)
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = ClientStaff
        fields = ['id', 'user', 'client', 'first_name', 'last_name', 'phone', 'address', 'city', 'state', 'zipcode']
