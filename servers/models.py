from django.db import models

from clients.models import Client
from vendors.models import Vendor


RAM_CHOICES = (
    ('1', '1 GB'),
    ('2', '2 GB'),
    ('4', '4 GB'),
    ('8', '8 GB'),
)

HARD_DRIVE_CHOICES = (
    ('h-1', 'SSD'),
    ('h-2', 'HDD'),
)

SERVER_TYPE_CHOICES = (
    ('t-1', 'Dedicated'),
    ('t-2', 'Virtual'),
    ('t-3', 'Cloud'),
)

SERVER_OS_CHOICES = (
    ('o-1', 'Windows'),
    ('o-2', 'Linux'),
    ('o-3', 'Mac'),
)

SERVER_STATUS_CHOICES = (
    ('s-1', 'Active'),
    ('s-2', 'Inactive'),
    ('s-3', 'Suspended'),
    ('s-4', 'Terminated'),
)

HARD_DISK_SIZE_CHOICES = (
    ('h-1', '1 TB'),
    ('h-2', '2 TB'),
)

CPU_CHOICES = (
    ('c-1', '1 Core'),
    ('c-2', '2 Core'),
)


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
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    app_platform = models.ForeignKey(AppPlatform, on_delete=models.CASCADE, blank=True, null=True)
    project_name = models.CharField(max_length=100, blank=True, null=True)
    memory = models.CharField(max_length=5, choices=RAM_CHOICES, blank=True, null=True)
    storage = models.CharField(max_length=5, choices=HARD_DRIVE_CHOICES, blank=True, null=True)
    os = models.CharField(max_length=5, choices=SERVER_OS_CHOICES, blank=True, null=True)
    server_type = models.CharField(max_length=5, choices=SERVER_TYPE_CHOICES, blank=True, null=True)
    public_ip = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(verbose_name='Hosted Region', max_length=100, blank=True, null=True)
    w_monitoring = models.BooleanField(verbose_name='Website Monitoring?', default=False)
    u_monitoring = models.BooleanField(verbose_name='Real User Monitoring?', default=False)
    p_monitoring = models.BooleanField(verbose_name='Performance Monitoring?', default=False)
    s_monitoring = models.BooleanField(verbose_name='Security Monitoring?', default=False)
    disc_utilization = models.CharField(max_length=100, blank=True, null=True)
    server_created = models.DateTimeField(blank=True, null=True)
    server_status = models.CharField(max_length=5, choices=SERVER_STATUS_CHOICES, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    server_charges = models.DecimalField(
        verbose_name='Server Consumption', max_digits=10, decimal_places=2, blank=True, null=True
    )

    def __str__(self):
        return f'{self.project_name}'

    def save(self, *args, **kwargs):
        if self.storage == 'h-1':
            if self.memory == '1':
                self.server_charges = 5
            elif self.memory == '2':
                self.server_charges = 10
            elif self.memory == '4':
                self.server_charges = 20
            elif self.memory == '8':
                self.server_charges = 40
        elif self.storage == 'h-2':
            if self.memory == '1':
                self.server_charges = 10
            elif self.memory == '2':
                self.server_charges = 20
            elif self.memory == '4':
                self.server_charges = 40
            elif self.memory == '8':
                self.server_charges = 80
        super(Server, self).save(*args, **kwargs)

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
    provider = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)

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
