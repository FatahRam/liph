# Generated by Django 3.2.8 on 2023-03-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wilaya',
            name='code_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
