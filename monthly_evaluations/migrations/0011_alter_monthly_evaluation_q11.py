# Generated by Django 3.2.8 on 2023-08-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_evaluations', '0010_auto_20230808_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_evaluation',
            name='q11',
            field=models.TextField(blank=True, null=True, verbose_name='Combien de pharmacies et de grossistes avez vous visités au cours du mois ?'),
        ),
    ]
