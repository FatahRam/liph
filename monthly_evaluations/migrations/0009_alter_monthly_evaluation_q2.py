# Generated by Django 3.2.8 on 2023-07-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_evaluations', '0008_monthly_evaluation_q2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_evaluation',
            name='q2',
            field=models.TextField(blank=True, null=True, verbose_name="Qui sont les médecins qui ont été visités plus d'une fois ce mois-ci, et la raison?"),
        ),
    ]
