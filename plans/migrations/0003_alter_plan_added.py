# Generated by Django 3.2.8 on 2022-07-12 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_alter_plan_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='added',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
