from django.contrib import admin
from .models import Server, HostingCompany, AppPlatform, MasterCredentials

admin.site.register(HostingCompany)
admin.site.register(AppPlatform)
admin.site.register(Server)
admin.site.register(MasterCredentials)
