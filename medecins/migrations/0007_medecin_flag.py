# Generated by Django 3.0.6 on 2020-07-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medecins', '0006_medecin_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='medecin',
            name='flag',
            field=models.BooleanField(default=False),
        ),
    ]
