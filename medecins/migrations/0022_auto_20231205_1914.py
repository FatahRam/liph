# Generated by Django 3.2.8 on 2023-12-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medecins', '0021_medecin_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medecin',
            name='adresse',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='medecin',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='medecin',
            name='telephone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
