# Generated by Django 3.2.8 on 2024-01-28 13:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('depenses', '0019_auto_20240110_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spend',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 1, 28, 13, 47, 37, 453631, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spendcomment',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 1, 28, 13, 47, 37, 454648, tzinfo=utc)),
        ),
    ]
