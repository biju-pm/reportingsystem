from django.db import models

from servers.models import Server


class Application(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
        ordering = ['name']

