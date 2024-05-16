# Generated by Django 5.0.6 on 2024-05-14 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rooms',
            options={'verbose_name': 'Room', 'verbose_name_plural': 'Rooms'},
        ),
        migrations.AlterField(
            model_name='hotel',
            name='closing_time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='opening_time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]