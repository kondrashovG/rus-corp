# Generated by Django 4.1.6 on 2023-03-25 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_customuser_on_vacation'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='account',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='Индивидуальный счет'),
        ),
    ]
