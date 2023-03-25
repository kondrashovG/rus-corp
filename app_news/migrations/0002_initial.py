# Generated by Django 4.1.6 on 2023-02-26 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_news', '0001_initial'),
        ('app_static_pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslink',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_static_pages.staticpage', verbose_name='ссылка на статическую страницу'),
        ),
        migrations.AddField(
            model_name='newslink',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_news.news', verbose_name='новость'),
        ),
    ]
