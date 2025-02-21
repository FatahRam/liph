# Generated by Django 3.2.8 on 2024-01-25 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaybookUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('number', models.PositiveIntegerField(verbose_name='Numéro')),
                ('still_using', models.BooleanField(default=True, verbose_name='Still Using')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Carnets De Versement',
            },
        ),
        migrations.CreateModel(
            name='Versement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('recu', models.CharField(max_length=200, verbose_name='Reçu')),
                ('somme', models.CharField(max_length=200, verbose_name='Somme')),
                ('en_reglement', models.CharField(max_length=200, verbose_name='En Réglement')),
                ('way_of_payment', models.CharField(choices=[('Chéque', 'Cheque'), ('Virement Bancaire', 'Virement')], default='Chéque', max_length=35, verbose_name='Type de paiement')),
                ('numero_de_cheque', models.CharField(max_length=100, verbose_name='Numéro de chéque')),
                ('attachement', models.FileField(blank=True, max_length=255, null=True, upload_to='versements', verbose_name='Piéce jointe')),
                ('paybook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='versement.paybookuser', verbose_name='Carnet')),
            ],
            options={
                'verbose_name_plural': 'Bons De Versements',
            },
        ),
    ]
