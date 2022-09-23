from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    public_key = models.CharField(max_length=200, blank=True, null=True)
    private_key = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'
        ordering = ['name']

