from django.db import models
from vendors.models import Vendor


class Domain(models.Model):
    name = models.CharField(max_length=200)
    is_purchased = models.BooleanField(default=False)
    first_optional_name = models.CharField(max_length=200, blank=True, null=True)
    second_optional_name = models.CharField(max_length=200, blank=True, null=True)
    provider = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Domain'
        verbose_name_plural = 'Domains'
        ordering = ['name']


class MailServer(models.Model):
    name = models.CharField(max_length=200)
    is_purchased = models.BooleanField(default=False)
    provider = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mail Server'
        verbose_name_plural = 'Mail Servers'
        ordering = ['name']
