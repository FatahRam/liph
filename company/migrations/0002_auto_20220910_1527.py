# Generated by Django 3.2.8 on 2022-09-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='bank_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='i_b_a_n',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='r_i_b',
            field=models.CharField(max_length=255),
        ),
    ]
