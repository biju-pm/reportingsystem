# Generated by Django 3.2 on 2022-10-06 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0003_remove_domain_application'),
        ('applications', '0005_appmonitoring_performancemonitoring'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domains.domain'),
        ),
    ]
