# Generated by Django 3.2.8 on 2024-01-29 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('versement', '0009_alter_versement_attachement'),
    ]

    operations = [
        migrations.AddField(
            model_name='versement',
            name='link',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Cloudinary links'),
        ),
    ]
