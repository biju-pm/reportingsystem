# Generated by Django 3.2 on 2022-09-29 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0005_vendor_is_approved'),
        ('domains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor'),
        ),
    ]