# Generated by Django 3.2.8 on 2023-11-21 13:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('depenses', '0013_auto_20231117_0347'),
    ]

    operations = [
        migrations.AddField(
            model_name='spend',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='spend',
            name='added',
            field=models.DateField(default=datetime.datetime(2023, 11, 21, 13, 4, 52, 427288, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spendcomment',
            name='added',
            field=models.DateField(default=datetime.datetime(2023, 11, 21, 13, 4, 52, 428128, tzinfo=utc)),
        ),
    ]
