# Generated by Django 3.2.8 on 2024-09-15 15:00

from django.db import migrations, models
import leaves.models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_arabe', models.CharField(max_length=255)),
                ('occasion_type', models.CharField(choices=[('RELIGIOUS', 'Religious'), ('NATIONAL', 'National')], max_length=10)),
                ('date', models.DateField()),
                ('video', models.FileField(blank=True, null=True, upload_to=leaves.models.get_holiday_video_upload_path)),
            ],
            options={
                'verbose_name': 'Occasion',
                'verbose_name_plural': 'Occasions',
            },
        ),
    ]
