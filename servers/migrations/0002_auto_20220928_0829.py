# Generated by Django 3.2 on 2022-09-28 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0005_vendor_is_approved'),
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sslcertificate',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor'),
        ),
        migrations.CreateModel(
            name='DnsRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('value', models.CharField(blank=True, max_length=100, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servers.server')),
            ],
            options={
                'verbose_name': 'DNS Record',
                'verbose_name_plural': 'DNS Records',
                'ordering': ['server'],
            },
        ),
    ]