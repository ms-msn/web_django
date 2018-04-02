# Generated by Django 2.0.3 on 2018-03-31 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_vacancy_vacancy_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsibility',
            name='name',
        ),
        migrations.AddField(
            model_name='responsibility',
            name='name_list',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='responsibility',
            name='vacancy_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]