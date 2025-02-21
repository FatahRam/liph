# Generated by Django 3.0.6 on 2020-06-11 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medecins', '0004_auto_20200604_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medecin',
            name='classification',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('f', 'F'), ('g', 'G'), ('p', 'P')], db_index=True, default='c', max_length=15),
        ),
        migrations.AlterField(
            model_name='medecin',
            name='nom',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='medecin',
            name='specialite',
            field=models.CharField(choices=[('Généraliste', 'Generaliste'), ('Diabetologue', 'Diabetologue'), ('Neurologue', 'Neurologue'), ('Psychologue', 'Psychologue'), ('Gynécologue ', 'Gynecologue'), ('Rumathologue', 'Rumathologue'), ('Allergologue ', 'Allergologue'), ('Phtisio', 'Phtisio'), ('Cardiologue', 'Cardiologue'), ('Urologue', 'Urologue'), ('Hematologue', 'Hematologue'), ('Orthopedie', 'Orthopedie'), ('Nutritionist', 'Nutritionist'), ('Dermatologue', 'Dermatologue'), ('Pharmacie', 'Pharmacie'), ('Grossiste', 'Grossiste')], db_index=True, default='Généraliste', max_length=15),
        ),
    ]
