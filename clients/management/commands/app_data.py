from django.core.management.base import BaseCommand

from applications.models import ApplicationType, AppPlatform, AppLanguage


class Command(BaseCommand):
    help = 'Populate the database with the following data'

    def handle(self, *args, **options):
        if ApplicationType.objects.count() == 0:
            try:
                ApplicationType.objects.bulk_create([
                    ApplicationType(name='Web Application'),
                    ApplicationType(name='Mobile Application'),
                    ApplicationType(name='Desktop Application'),
                    ApplicationType(name='API'),
                    ApplicationType(name='Database'),
                    ApplicationType(name='Other'),
                ])
            except Exception as e:
                print(e)
            try:
                AppPlatform.objects.bulk_create([
                    AppPlatform(name='Linux'),
                    AppPlatform(name='Windows'),
                    AppPlatform(name='Mac'),
                    AppPlatform(name='Android'),
                    AppPlatform(name='iOS'),
                    AppPlatform(name='Windows Phone'),
                    AppPlatform(name='Web'),
                    AppPlatform(name='Other'),
                ])
            except Exception as e:
                print(e)

            try:
                AppLanguage.objects.bulk_create([
                    AppLanguage(name='Python'),
                    AppLanguage(name='PHP'),
                    AppLanguage(name='Ruby'),
                    AppLanguage(name='WordPress'),
                    AppLanguage(name='Craft CMS'),
                    AppLanguage(name='Laravel'),
                    AppLanguage(name='Other'),
                ])
            except Exception as e:
                print(e)
