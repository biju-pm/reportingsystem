from django.db import models

from clients.models import Client


class Payment(models.Model):
    client = models.ForeignKey(
        Client, related_name='payments', on_delete=models.CASCADE
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)

    class Meta:
        ordering = ['-created_on']
