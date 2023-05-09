# Generated by Django 4.1.3 on 2022-12-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_event_about_1_delete_event_about_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='month',
            field=models.CharField(choices=[('01', 'Января'), ('02', 'Февраля'), ('03', 'Марта'), ('04', 'Апреля'), ('05', 'Мая'), ('06', 'Июня'), ('07', 'Июля'), ('08', 'Августа'), ('09', 'Сентября'), ('10', 'Октября'), ('11', 'Ноября'), ('12', 'Декабря')], default='01', max_length=2, verbose_name='Месяц'),
        ),
    ]
