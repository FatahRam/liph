# Generated by Django 3.2.8 on 2022-09-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('adress', models.CharField(max_length=255)),
                ('r_c', models.CharField(max_length=255)),
                ('fiscal_id', models.CharField(max_length=255)),
                ('a_i', models.CharField(max_length=255)),
                ('n_i_s', models.CharField(max_length=255)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_2', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_3', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_4', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_2', models.EmailField(max_length=255)),
                ('bank_name', models.EmailField(max_length=255)),
                ('r_i_b', models.EmailField(max_length=255)),
                ('i_b_a_n', models.EmailField(max_length=255)),
            ],
        ),
    ]
