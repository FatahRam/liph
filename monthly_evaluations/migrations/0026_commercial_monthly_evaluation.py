# Generated by Django 3.2.8 on 2024-07-29 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monthly_evaluations', '0025_auto_20240402_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commercial_Monthly_Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateField(blank=True, db_index=True, default=django.utils.timezone.now)),
                ('sup_evaluation', models.BooleanField(default=False, verbose_name="Le superviseur à fait l'évaluation du délégué")),
                ('user_sup_evaluation', models.BooleanField(default=True, verbose_name='Le délégué à évalué son superviseur')),
                ('user_direction_evaluation', models.BooleanField(default=False, verbose_name="La direction à consulté l'évaluation")),
                ('own_perc', models.CharField(blank=True, max_length=200, null=True, verbose_name='Pourcentage')),
                ('q1', models.PositiveIntegerField(blank=True, null=True)),
                ('q2', models.TextField(blank=True, null=True)),
                ('q3', models.TextField(blank=True, null=True)),
                ('q4', models.TextField(blank=True, null=True)),
                ('q5', models.TextField(blank=True, null=True)),
                ('q6', models.TextField(blank=True, null=True)),
                ('q7', models.TextField(blank=True, null=True)),
                ('q8', models.TextField(blank=True, null=True)),
                ('q9', models.TextField(blank=True, null=True)),
                ('q10', models.TextField(blank=True, null=True)),
                ('updatable', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
