# Generated by Django 5.1.7 on 2025-04-14 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='hourly_rate',
            new_name='weekly_rate',
        ),
    ]
