from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.conf import settings

APPROVAL_CHOICES = (
                ('t-1', 'Approved'),
                ('t-2', 'Pending'),
                ('t-3', 'Rejected'),
                )


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_account_manager_web = models.BooleanField(default=False)
    is_account_manager_digital = models.BooleanField(default=False)
    is_project_manager_web = models.BooleanField(default=False)
    is_project_manager_digital = models.BooleanField(default=False)
    is_team_lead_web = models.BooleanField(default=False)
    is_team_lead_digital = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    is_tester = models.BooleanField(default=False)
    is_designer = models.BooleanField(default=False)
    is_seo = models.BooleanField(default=False)
    is_approved = models.CharField(max_length=10,
                                   choices=APPROVAL_CHOICES,
                                   default='t-1')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.user.username


def post_save_subscription_receiver(sender, instance, created, *args, **kwargs):
    if created:
        new_profile = Profile.objects.get_or_create(user=instance)
        print(new_profile)


post_save.connect(post_save_subscription_receiver, sender=settings.AUTH_USER_MODEL)