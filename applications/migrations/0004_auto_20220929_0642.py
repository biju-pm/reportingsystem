# Generated by Django 3.2 on 2022-09-29 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20220929_0602'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'App Language',
                'verbose_name_plural': 'App Languages',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AppPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'App Platform',
                'verbose_name_plural': 'App Platforms',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='application',
            name='AppLanguage_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='applications.applanguage'),
        ),
    ]
