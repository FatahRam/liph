# Generated by Django 3.2.8 on 2022-11-26 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plans', '0018_auto_20220901_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='client_validation_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_validated_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='plan',
            name='commune_validation_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commune_validated_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='plan',
            name='tasks_validation_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks_validated_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
