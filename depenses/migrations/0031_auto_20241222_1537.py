# Generated by Django 3.2.8 on 2024-12-22 14:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('depenses', '0030_auto_20241222_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spend',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 12, 22, 14, 37, 32, 38473, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spend',
            name='approved_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spendcomment',
            name='added',
            field=models.DateField(default=datetime.datetime(2024, 12, 22, 14, 37, 32, 39622, tzinfo=utc)),
        ),
    ]
