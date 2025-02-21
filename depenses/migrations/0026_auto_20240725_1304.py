# Generated by Django 3.2.8 on 2024-07-25 12:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('depenses', '0025_auto_20240725_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spend',
            name='url',
        ),
        migrations.AlterField(
            model_name='spend',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 7, 25, 12, 4, 23, 610602, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spendcomment',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 7, 25, 12, 4, 23, 618451, tzinfo=utc)),
        ),
    ]
