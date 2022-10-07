from django.db import models

from servers.models import Server
from domains.models import Domain, MailServer


class AppLanguage(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'App Language'
        verbose_name_plural = 'App Languages'
        ordering = ['name']


class AppPlatform(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'App Platform'
        verbose_name_plural = 'App Platforms'
        ordering = ['name']


class ApplicationType(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Application Type'
        verbose_name_plural = 'Application Types'
        ordering = ['name']


class Application(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, blank=True, null=True)
    application_type = models.ForeignKey(ApplicationType, on_delete=models.CASCADE, blank=True, null=True)
    AppLanguage_language = models.ForeignKey(AppLanguage, on_delete=models.CASCADE, blank=True, null=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, blank=True, null=True)
    mail_server = models.ForeignKey(MailServer, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
        ordering = ['name']


class AppMonitoring(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.application.name

    class Meta:
        verbose_name = 'App Monitoring'
        verbose_name_plural = 'App Monitoring'
        ordering = ['application']


class PerformanceMonitoring(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    cpu = models.BooleanField(default=True)
    memory = models.BooleanField(default=True)
    disk = models.BooleanField(default=True)
    network = models.BooleanField(default=True)

    def __str__(self):
        return self.application.name

    class Meta:
        verbose_name = 'Performance Monitoring'
        verbose_name_plural = 'Performance Monitoring'
        ordering = ['application']
