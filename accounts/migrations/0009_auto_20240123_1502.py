# Generated by Django 3.2.8 on 2024-01-23 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20240121_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_human',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='entry_date',
            field=models.DateField(default=datetime.date(2024, 1, 23)),
        ),
    ]
