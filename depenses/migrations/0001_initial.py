# Generated by Django 3.2.8 on 2023-11-17 01:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Spend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateField(default=datetime.datetime(2023, 11, 17, 1, 9, 18, 766063, tzinfo=utc))),
                ('log_number', models.PositiveIntegerField()),
                ('spend_type', models.TextField(choices=[('Déplacement', 'Déplacement'), ('Semi-déplacement', 'Semi-déplacement'), ('Autre', 'Autre')], max_length=20)),
                ('departure', models.TextField(blank=True, max_length=50, null=True)),
                ('arrival', models.TextField(blank=True, max_length=50, null=True)),
                ('distance', models.TextField(blank=True, max_length=50, null=True)),
                ('other_spend_reason', models.TextField(blank=True, max_length=1000, null=True)),
                ('spender', models.TextField(max_length=1000)),
                ('attachement', models.FileField(blank=True, max_length=255, null=True, upload_to='spends')),
                ('price', models.PositiveIntegerField()),
                ('price_in_letters', models.TextField(blank=True, null=True)),
                ('way_of_payment', models.TextField(choices=[('Chéque', 'Chéque'), ('Virement bancaire', 'Virement bancaire'), ('Espèces', 'Espèces')], max_length=20, null=True)),
                ('nature_depense', models.TextField(blank=True, max_length=2000, null=True)),
                ('status', models.TextField(choices=[('Non confirmé', 'Non confirmé'), ('Confirmé', 'Confirmé')], default='Non confirmé', max_length=20)),
                ('administration_comment', models.TextField(blank=True, default='-', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpendComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateField(default=datetime.datetime(2023, 11, 17, 1, 9, 18, 767121, tzinfo=utc))),
                ('comment', models.TextField(blank=True, max_length=2000, null=True)),
                ('spend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depenses.spend')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
