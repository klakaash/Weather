# Generated by Django 3.1.5 on 2021-02-06 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0003_auto_20210206_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='city',
            new_name='city_name',
        ),
    ]
