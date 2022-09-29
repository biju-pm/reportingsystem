from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clients.urls')),
    path('', include('accounts.urls')),
    path('', include('departments.urls')),
    path('', include('vendors.urls')),
    path('', include('applications.urls')),
    path('', include('servers.urls')),
    path('', include('domains.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

]

admin.site.site_header = "Reporting System Administration"
admin.site.site_title = "Reporting System Admin Portal"
admin.site.index_title = "Welcome to Reporting System Admin Portal"
