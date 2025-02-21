# Generated by Django 3.2.8 on 2024-02-01 11:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('depenses', '0022_auto_20240201_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spend',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 2, 1, 11, 39, 25, 857086, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spendcomment',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 2, 1, 11, 39, 25, 858057, tzinfo=utc)),
        ),
    ]
