# Generated by Django 5.1.7 on 2025-04-14 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0002_rename_hourly_rate_bike_weekly_rate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bike',
            new_name='Bikes',
        ),
    ]
