# Generated by Django 3.2.8 on 2024-11-27 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0007_rename_rh_délégue_representant'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Délégue_Representant',
        ),
    ]
