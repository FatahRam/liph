# Generated by Django 3.2.8 on 2022-09-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0016_auto_20220831_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='valid_clients',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='plan',
            name='valid_commune',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='plan',
            name='valid_tasks',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
