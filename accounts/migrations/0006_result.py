# Generated by Django 3.1 on 2020-09-20 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_account_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_id', models.CharField(max_length=20)),
                ('stud_reg_no', models.CharField(max_length=20)),
                ('total_marks', models.CharField(max_length=20)),
                ('obtain_marks', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('stud_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
    ]
