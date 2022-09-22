from django.db import models
from django.conf import settings
from departments.models import Department

User = settings.AUTH_USER_MODEL


class AccountsManager(models.Model):
    user = models.OneToOneField(User,
                                related_name='accounts_manager_digital',
                                on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ProjectManager(models.Model):
    user = models.OneToOneField(User,
                                related_name='project_manager_digital',
                                on_delete=models.CASCADE)
    team = models.ForeignKey(AccountsManager, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class TeamLead(models.Model):
    user = models.OneToOneField(User,
                                related_name='team_lead_digital',
                                on_delete=models.CASCADE)
    team = models.ForeignKey(ProjectManager, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class SeoStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(TeamLead, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

