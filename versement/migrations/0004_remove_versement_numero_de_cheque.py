# Generated by Django 3.2.8 on 2024-01-25 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('versement', '0003_versement_numero_de_cheque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='versement',
            name='numero_de_cheque',
        ),
    ]
