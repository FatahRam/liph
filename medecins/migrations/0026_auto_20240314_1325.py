# Generated by Django 3.2.8 on 2024-03-14 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medecins', '0025_medecin_wilaya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medecin',
            name='specialite',
            field=models.CharField(choices=[('Généraliste', 'Generaliste'), ('Diabetologue', 'Diabetologue'), ('Neurologue', 'Neurologue'), ('Psychologue', 'Psychologue'), ('Gynécologue', 'Gynecologue'), ('Rumathologue', 'Rumathologue'), ('Allergologue ', 'Allergologue'), ('Phtisio', 'Phtisio'), ('Cardiologue', 'Cardiologue'), ('Urologue', 'Urologue'), ('Hematologue', 'Hematologue'), ('Orthopedie', 'Orthopedie'), ('Nutritionist', 'Nutritionist'), ('Dermatologue', 'Dermatologue'), ('Interniste', 'Interniste'), ('Pharmacie', 'Pharmacie'), ('Grossiste', 'Grossiste'), ('SuperGros', 'Supergros'), ('Gastrologue', 'Gastrologue'), ('Endocrinologue', 'Endocrinologue'), ('Dentiste', 'Dentiste'), ('ORL', 'Orl'), ('Maxilo facial', 'Maxilo Facial')], db_index=True, default='Généraliste', max_length=15),
        ),
        migrations.CreateModel(
            name='MedecinModificationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('medecin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medecins.medecin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('users_after', models.ManyToManyField(related_name='users_after_modification', to=settings.AUTH_USER_MODEL)),
                ('users_before', models.ManyToManyField(related_name='users_before_modification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
