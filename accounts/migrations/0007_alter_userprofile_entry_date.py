# Generated by Django 3.2.8 on 2023-12-01 01:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_userprofile_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='entry_date',
            field=models.DateField(default=datetime.date(2023, 12, 1)),
        ),
    ]
