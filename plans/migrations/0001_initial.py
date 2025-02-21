# Generated by Django 3.2.8 on 2022-07-11 19:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medecins', '0013_auto_20211130_0917'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateField(default=datetime.datetime(2022, 7, 11, 19, 12, 34, 215927))),
                ('valid', models.BooleanField(default=False)),
                ('clients', models.ManyToManyField(to='medecins.Medecin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
