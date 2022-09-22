# Generated by Django 3.2 on 2022-09-21 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20220920_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='cpu',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='disc_utilization',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='memory',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='os_details',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='public_ip',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='storage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Hosted Region'),
        ),
        migrations.CreateModel(
            name='SslCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Provider Name')),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.server')),
            ],
            options={
                'verbose_name': 'SSL Certificate',
                'verbose_name_plural': 'SSL Certificates',
                'ordering': ['server'],
            },
        ),
        migrations.CreateModel(
            name='SshCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.server')),
            ],
            options={
                'verbose_name': 'SSH Credentials',
                'verbose_name_plural': 'SSH Credentials',
                'ordering': ['server'],
            },
        ),
        migrations.CreateModel(
            name='MasterCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.server')),
            ],
            options={
                'verbose_name': 'Master Credentials',
                'verbose_name_plural': 'Master Credentials',
                'ordering': ['server'],
            },
        ),
    ]