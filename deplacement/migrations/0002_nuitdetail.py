# Generated by Django 3.2.8 on 2025-01-14 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deplacement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NuitDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nuit', models.PositiveIntegerField(verbose_name='Nuit numéro')),
                ('start_date', models.DateField(verbose_name='Date de début')),
                ('end_date', models.DateField(verbose_name='Date de fin')),
                ('deplacement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nuits_details', to='deplacement.deplacement')),
            ],
            options={
                'verbose_name': 'Détail de nuitée',
                'verbose_name_plural': 'Détails des nuitées',
            },
        ),
    ]
