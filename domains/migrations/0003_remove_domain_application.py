# Generated by Django 3.2 on 2022-10-06 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0002_domain_provider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domain',
            name='application',
        ),
    ]