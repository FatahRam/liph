# Generated by Django 3.2.8 on 2022-08-20 16:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plans', '0006_auto_20220820_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='valid',
            new_name='valid_clients',
        ),
        migrations.AddField(
            model_name='plan',
            name='valid_commune',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='plan',
            unique_together={('day', 'user')},
        ),
    ]
