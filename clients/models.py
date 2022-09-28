import random
from django.db import models
from django.core.exceptions import ValidationError
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


class Ticket(models.Model):
    subject = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=100, blank=True, null=True)
    ticket_status = models.CharField(max_length=100, blank=True, null=True)
    ticket_priority = models.CharField(max_length=100, blank=True, null=True)
    ticket_type = models.CharField(max_length=100, blank=True, null=True)
    ticket_due_date = models.DateTimeField(blank=True, null=True)
    ticket_assigned_date = models.DateTimeField(blank=True, null=True)
    ticket_resolved_date = models.DateTimeField(blank=True, null=True)
    ticket_resolved_by = models.ManyToManyField(User, blank=True, related_name='ticket_resolved_by')
    ticket_assigned_to = models.ManyToManyField(User, blank=True, related_name='ticket_assigned_to')
    ticket_created_by = models.ForeignKey(User,
                                          on_delete=models.CASCADE,
                                          blank=True, null=True,
                                          related_name='ticket_created_by'
                                          )
    ticket_updated_by = models.ForeignKey(User,
                                          on_delete=models.CASCADE,
                                          blank=True, null=True,
                                          related_name='ticket_updated_by'
                                          )

    time_taken = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.client.user.email

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ['created_at']

    # def calculate_time_taken(self, instance):
    #     time_taken = instance.ticket_resolved_date - instance.ticket_assigned_date
    #     instance.time_taken = time_taken
    #     instance.save()

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = str(1000 + Ticket.objects.count())
        if self.ticket_resolved_date:
            try:
                time_taken = self.ticket_resolved_date - self.ticket_assigned_date
                self.time_taken = time_taken
            except TypeError as e:
                pass
        super(Ticket, self).save(*args, **kwargs)

    def clean(self):
        # if self.ticket_assigned_to.count() > 1:
        #     raise ValidationError('Only one user can be assigned to a ticket')
        # if self.ticket_resolved_by.count() > 1:
        #     raise ValidationError('Only one user can resolve a ticket')
        if self.ticket_resolved_date:
            try:
                if self.ticket_resolved_date < self.ticket_assigned_date:
                    raise ValidationError('Ticket resolved date cannot be less than ticket assigned date')
            except TypeError as e:
                pass


class ClientStaff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Client Staff'
        verbose_name_plural = 'Client Staff'
        ordering = ['user']
