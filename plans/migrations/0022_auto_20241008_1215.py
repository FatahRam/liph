# Generated by Django 3.2.8 on 2024-10-08 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plans', '0021_auto_20221208_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantask',
            name='is_transferred',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='plantask',
            name='transferred_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='plantask',
            name='transferred_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
