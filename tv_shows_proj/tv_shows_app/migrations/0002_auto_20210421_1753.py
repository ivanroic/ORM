# Generated by Django 2.2.4 on 2021-04-21 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateTimeField(verbose_name='%Y-%m-%d'),
        ),
    ]
