# Generated by Django 3.2.8 on 2022-08-29 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0010_plan_isfree'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='valid_tasks',
            field=models.BooleanField(default=False),
        ),
    ]
