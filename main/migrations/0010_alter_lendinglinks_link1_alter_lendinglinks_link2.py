# Generated by Django 4.1.3 on 2022-12-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_lendinglinks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lendinglinks',
            name='link1',
            field=models.CharField(default='#', max_length=250, verbose_name='Ссылка баннер'),
        ),
        migrations.AlterField(
            model_name='lendinglinks',
            name='link2',
            field=models.CharField(default='#', max_length=250, verbose_name='Ссылка ноутбук'),
        ),
    ]