# Generated by Django 3.2.8 on 2024-02-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('versement', '0015_auto_20240208_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='creance',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
