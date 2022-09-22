from django.db import models
from django.conf import settings
from departments.models import Department
User = settings.AUTH_USER_MODEL


class Client(models.Model):
    user = models.OneToOneField(User,
                                related_name='client',
                                on_delete=models.CASCADE)
    department = models.ManyToManyField(Department,
                                        related_name='clients',
                                        blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        try:
            return self.user.email
        except Exception as e:
            return self.name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['name']


class HostingCompany(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hosting Company'
        verbose_name_plural = 'Hosting Companies'
        ordering = ['name']


class AppPlatform(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'App Platform'
        verbose_name_plural = 'App Platforms'
        ordering = ['name']


class Server(models.Model):
    hosting_company = models.ForeignKey(HostingCompany, on_delete=models.CASCADE, blank=True, null=True)
    app_platform = models.ForeignKey(AppPlatform, on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField(verbose_name='Hosted Region', max_length=100, blank=True, null=True)
    project_name = models.CharField(max_length=100, blank=True, null=True)
    server_size = models.CharField(max_length=100, blank=True, null=True)
    cpu = models.CharField(max_length=100, blank=True, null=True)
    memory = models.CharField(max_length=100, blank=True, null=True)
    storage = models.CharField(max_length=100, blank=True, null=True)
    disc_utilization = models.CharField(max_length=100, blank=True, null=True)
    os_details = models.CharField(max_length=100, blank=True, null=True)
    public_ip = models.CharField(max_length=100, blank=True, null=True)
    monitoring = models.BooleanField(verbose_name='Advanced Monitoring?', default=False)
    server_created = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.client.name

    class Meta:
        verbose_name = 'Server'
        verbose_name_plural = 'Servers'
        ordering = ['created']


class MasterCredentials(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return self.server.client.name

    class Meta:
        verbose_name = 'Master Credentials'
        verbose_name_plural = 'Master Credentials'
        ordering = ['server']


class SslCertificate(models.Model):
    name = models.CharField(verbose_name='Provider Name', max_length=100, blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return self.server.client.name

    class Meta:
        verbose_name = 'SSL Certificate'
        verbose_name_plural = 'SSL Certificates'
        ordering = ['server']


class SshCredentials(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return self.server.client.name

    class Meta:
        verbose_name = 'SSH Credentials'
        verbose_name_plural = 'SSH Credentials'
        ordering = ['server']


class Ticket(models.Model):
    subject = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.client.user.email

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ['created']
