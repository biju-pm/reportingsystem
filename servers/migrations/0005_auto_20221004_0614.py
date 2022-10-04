# Generated by Django 3.2 on 2022-10-04 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0016_auto_20220927_0558'),
        ('vendors', '0005_vendor_is_approved'),
        ('servers', '0004_auto_20220929_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='cpu',
        ),
        migrations.RemoveField(
            model_name='server',
            name='hosting_company',
        ),
        migrations.RemoveField(
            model_name='server',
            name='os_details',
        ),
        migrations.RemoveField(
            model_name='server',
            name='server_size',
        ),
        migrations.AddField(
            model_name='server',
            name='os',
            field=models.CharField(blank=True, choices=[('o-1', 'Windows'), ('o-2', 'Linux'), ('o-3', 'Mac')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='server_charges',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='server_status',
            field=models.CharField(blank=True, choices=[('s-1', 'Active'), ('s-2', 'Inactive'), ('s-3', 'Suspended'), ('s-4', 'Terminated')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='server_type',
            field=models.CharField(blank=True, choices=[('t-1', 'Dedicated'), ('t-2', 'Virtual'), ('t-3', 'Cloud')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor'),
        ),
        migrations.AlterField(
            model_name='server',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
        migrations.AlterField(
            model_name='server',
            name='memory',
            field=models.CharField(blank=True, choices=[('1', '1 GB'), ('2', '2 GB'), ('4', '4 GB'), ('8', '8 GB')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='storage',
            field=models.CharField(blank=True, choices=[('h-1', 'SSD'), ('h-2', 'HDD')], max_length=5, null=True),
        ),
    ]