# Generated by Django 3.2.8 on 2024-07-25 12:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('depenses', '0026_auto_20240725_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='spend',
            name='url',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='spend',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 7, 25, 12, 5, 1, 845057, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spendcomment',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 7, 25, 12, 5, 1, 846875, tzinfo=utc)),
        ),
    ]
