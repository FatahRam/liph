# Generated by Django 3.2.8 on 2024-01-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('versement', '0012_auto_20240129_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paybookuser',
            name='number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Numéro du Carnet'),
        ),
        migrations.AlterField(
            model_name='versement',
            name='way_of_payment',
            field=models.CharField(choices=[('annulé', 'Annule'), ('Chéque', 'Cheque'), ('Virement Bancaire', 'Virement'), ('Espéce', 'Espece')], default='Chéque', max_length=35, verbose_name='Type de paiement'),
        ),
    ]
