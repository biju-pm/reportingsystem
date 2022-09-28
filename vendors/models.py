from django.db import models


class VendorCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vendor Category'
        verbose_name_plural = 'Vendor Categories'
        ordering = ['name']


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(VendorCategory, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'
        ordering = ['name']


class ApiKeys(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)
    api_key = models.CharField(max_length=200, blank=True, null=True)
    api_secret = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.vendor.name

    class Meta:
        verbose_name = 'Api Key'
        verbose_name_plural = 'Api Keys'
        ordering = ['vendor']
