# Generated by Django 4.1.6 on 2023-03-25 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_accounts', '0001_initial'),
        ('app_users', '0004_alter_customuser_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_accounts.account'),
        ),
    ]
