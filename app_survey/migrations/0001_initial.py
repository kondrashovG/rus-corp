# Generated by Django 4.1.6 on 2023-02-26 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='заголовок')),
                ('text', models.TextField(max_length=4096, verbose_name='текст')),
                ('visible', models.BooleanField(default=False, verbose_name='видимый на сайте')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='дата публикации')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='дата окончания')),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'вопросы',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='текст')),
                ('votes', models.IntegerField(default=0, verbose_name='количество голосов')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_survey.question', verbose_name='вопрос')),
            ],
            options={
                'verbose_name': 'вариант ответа',
                'verbose_name_plural': 'варианты ответов',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_survey.choice', verbose_name='выбор')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_survey.question', verbose_name='вопрос')),
            ],
            options={
                'verbose_name': 'ответ',
                'verbose_name_plural': 'ответы',
                'ordering': ['-created'],
            },
        ),
    ]