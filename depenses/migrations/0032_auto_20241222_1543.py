# Generated by Django 3.2.8 on 2024-12-22 14:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('depenses', '0031_auto_20241222_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spend',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 12, 22, 14, 43, 32, 532974, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spendcomment',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 12, 22, 14, 43, 32, 534290, tzinfo=utc)),
        ),
    ]
