# Generated by Django 3.1 on 2020-09-18 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='profile',
        ),
    ]
