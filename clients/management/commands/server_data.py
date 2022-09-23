from django.core.management.base import BaseCommand

from servers.models import HostingCompany, AppPlatform


class Command(BaseCommand):
    help = 'Populate the database with the following data'

    def handle(self, *args, **options):
        if HostingCompany.objects.count() == 0:
            try:
                HostingCompany.objects.bulk_create([
                    HostingCompany(name='Digital Ocean'),
                    HostingCompany(name='Linode'),
                    HostingCompany(name='AWS'),
                    HostingCompany(name='Google Cloud'),
                ])
            except Exception as e:
                print(e)
            try:
                AppPlatform.objects.bulk_create([
                    AppPlatform(name='Python'),
                    AppPlatform(name='Node'),
                    AppPlatform(name='Ruby'),
                    AppPlatform(name='PHP'),
                    AppPlatform(name='Wordpress'),
                    AppPlatform(name='Laravel'),
                ])
            except Exception as e:
                print(e)
