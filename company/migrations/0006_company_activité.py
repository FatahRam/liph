# Generated by Django 3.2.8 on 2024-01-24 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_company_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='activité',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
