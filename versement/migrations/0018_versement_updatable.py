# Generated by Django 3.2.8 on 2024-03-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('versement', '0017_auto_20240225_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='versement',
            name='updatable',
            field=models.BooleanField(default=False),
        ),
    ]
