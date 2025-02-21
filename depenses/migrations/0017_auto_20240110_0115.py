# Generated by Django 3.2.8 on 2024-01-10 00:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('depenses', '0016_auto_20231201_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spend',
            name='log_number',
        ),
        migrations.AlterField(
            model_name='spend',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 1, 10, 0, 15, 40, 129578, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spendcomment',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 1, 10, 0, 15, 40, 130595, tzinfo=utc)),
        ),
    ]
