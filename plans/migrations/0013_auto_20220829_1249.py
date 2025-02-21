# Generated by Django 3.2.8 on 2022-08-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0012_plantask'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plantask',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='plantask',
            name='order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
