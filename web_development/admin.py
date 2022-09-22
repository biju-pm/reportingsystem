from django.contrib import admin
from .models import *

admin.site.register(AccountsManager)
admin.site.register(ProjectManager)
admin.site.register(TeamLead)
admin.site.register(Designer)
admin.site.register(Developer)
admin.site.register(Tester)