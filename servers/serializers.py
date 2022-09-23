from rest_framework import serializers

from .models import Server, MasterCredentials, SslCertificate, SshCredentials, HostingCompany, AppPlatform


class MasterCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterCredentials
        fields = ('username', 'password', 'server')

        depth = 1


class SslCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SslCertificate
        fields = ('name', 'expiry_date', 'server')


class SshCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SshCredentials
        fields = ('username', 'password', 'server')


class HostingCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = HostingCompany
        fields = ['id', 'name']


class AppPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppPlatform
        fields = ['id', 'name']


class ServerSerializer(serializers.ModelSerializer):
    mastercredentials_set = MasterCredentialsSerializer(many=True, read_only=True)
    sslcertificate_set = SslCertificateSerializer(many=True, read_only=True)
    sshcredentials_set = SshCredentialsSerializer(many=True, read_only=True)
    hosting_company = serializers.CharField(source='hosting_company.name')
    app_platform = serializers.CharField(source='app_platform.name')

    class Meta:
        model = Server
        fields = ['hosting_company', 'app_platform', 'location', 'project_name', 'server_size', 'cpu', 'memory',
                  'storage', 'disc_utilization', 'os_details', 'public_ip', 'monitoring', 'server_created',
                  'created', 'updated', 'client', 'mastercredentials_set', 'sslcertificate_set', 'sshcredentials_set']

