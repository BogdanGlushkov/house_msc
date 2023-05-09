# Generated by Django 4.1.3 on 2022-12-04 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_lendinglinks_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New', max_length=50, verbose_name='Название')),
                ('description', models.CharField(max_length=250, verbose_name='Описание вакансии')),
                ('salary', models.IntegerField(verbose_name='Заработная плата')),
                ('salaryDesc', models.CharField(default='смена', max_length=25, verbose_name='Время заработка')),
                ('link', models.CharField(default='https://t.me/chausmoscow_bot', max_length=250, verbose_name='Ссылка на вакансию')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.AlterModelOptions(
            name='lendinglinks',
            options={'verbose_name': 'Ссылки на странице', 'verbose_name_plural': 'Ссылки'},
        ),
    ]
