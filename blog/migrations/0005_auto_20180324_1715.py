# Generated by Django 2.0.3 on 2018-03-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180324_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hh_vacancy',
            name='responsibility',
            field=models.TextField(blank=True, null=True),
        ),
    ]
