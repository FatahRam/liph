# Generated by Django 3.2.8 on 2024-10-14 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20241010_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='can_receive_tasks',
            new_name='can_send_receive_tasks',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='entry_date',
            field=models.DateField(default=datetime.date(2024, 10, 14)),
        ),
    ]
