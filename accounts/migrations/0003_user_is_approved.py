# Generated by Django 3.2 on 2022-03-25 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220325_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_approved',
            field=models.CharField(choices=[('t-1', 'Approved'), ('t-2', 'Pending'), ('t-3', 'Rejected')], default='t-1', max_length=10),
        ),
    ]