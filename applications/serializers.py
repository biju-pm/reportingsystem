from rest_framework import serializers
from .models import Application, ApplicationType, AppLanguage
from servers.models import Server
from domains.models import Domain, MailServer


class ApplicationSerializer(serializers.ModelSerializer):
    server = serializers.SlugRelatedField(queryset=Server.objects.all(), slug_field='project_name')
    application_type = serializers.SlugRelatedField(queryset=ApplicationType.objects.all(), slug_field='name')
    AppLanguage_language = serializers.SlugRelatedField(queryset=AppLanguage.objects.all(), slug_field='name')
    domain = serializers.SlugRelatedField(queryset=Domain.objects.all(), slug_field='name')
    mail_server = serializers.SlugRelatedField(queryset=MailServer.objects.all(), slug_field='name')

    class Meta:
        model = Application
        fields = ['id', 'name', 'description', 'server', 'application_type', 'AppLanguage_language', 'domain',
                  'mail_server']
