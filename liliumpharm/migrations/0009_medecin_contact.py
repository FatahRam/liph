# Generated by Django 3.0.6 on 2020-08-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medecins', '0008_medecin_updatable'),
    ]

    operations = [
        migrations.AddField(
            model_name='medecin',
            name='contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
