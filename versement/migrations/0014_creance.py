# Generated by Django 3.2.8 on 2024-02-08 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('versement', '0013_auto_20240130_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('attachement', models.FileField(blank=True, max_length=255, null=True, upload_to='versements', verbose_name='Piéce jointe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
