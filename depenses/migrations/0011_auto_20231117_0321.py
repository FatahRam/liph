# Generated by Django 3.2.8 on 2023-11-17 02:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('depenses', '0010_auto_20231117_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spend',
            name='added',
            field=models.DateField(default=datetime.datetime(2023, 11, 17, 2, 21, 26, 664843, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spendcomment',
            name='added',
            field=models.DateField(default=datetime.datetime(2023, 11, 17, 2, 21, 26, 665607, tzinfo=utc)),
        ),
    ]
