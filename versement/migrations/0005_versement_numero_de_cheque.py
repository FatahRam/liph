# Generated by Django 3.2.8 on 2024-01-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('versement', '0004_remove_versement_numero_de_cheque'),
    ]

    operations = [
        migrations.AddField(
            model_name='versement',
            name='numero_de_cheque',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Numéro de chéque'),
        ),
    ]
