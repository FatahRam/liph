# Generated by Django 3.2.8 on 2023-11-17 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateField(auto_now_add=True)),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(max_length=255)),
                ('cost', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DealComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DealStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DealType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DealProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtt', models.PositiveIntegerField()),
                ('deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deals.deal')),
            ],
        ),
    ]
