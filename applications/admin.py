from django.contrib import admin
from .models import Application, ApplicationType, AppPlatform, AppLanguage


admin.site.register(Application)
admin.site.register(ApplicationType)
admin.site.register(AppPlatform)
admin.site.register(AppLanguage)
