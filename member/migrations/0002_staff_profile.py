# Generated by Django 3.1 on 2020-09-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='profile',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
