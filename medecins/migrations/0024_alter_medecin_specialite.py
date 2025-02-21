# Generated by Django 3.2.8 on 2024-01-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medecins', '0023_auto_20231206_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medecin',
            name='specialite',
            field=models.CharField(choices=[('Généraliste', 'Generaliste'), ('Diabetologue', 'Diabetologue'), ('Neurologue', 'Neurologue'), ('Psychologue', 'Psychologue'), ('Gynécologue', 'Gynecologue'), ('Rumathologue', 'Rumathologue'), ('Allergologue ', 'Allergologue'), ('Phtisio', 'Phtisio'), ('Cardiologue', 'Cardiologue'), ('Urologue', 'Urologue'), ('Hematologue', 'Hematologue'), ('Orthopedie', 'Orthopedie'), ('Nutritionist', 'Nutritionist'), ('Dermatologue', 'Dermatologue'), ('Interniste', 'Interniste'), ('Pharmacie', 'Pharmacie'), ('Grossiste', 'Grossiste'), ('SuperGros', 'Supergros'), ('Gastrologue', 'Gastrologue'), ('Endocrinologue', 'Endocrinologue'), ('Dentiste', 'Dentiste'), ('ORL', 'Orl')], db_index=True, default='Généraliste', max_length=15),
        ),
    ]
