# Generated by Django 5.1.7 on 2025-05-08 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0013_bikes_image_2_bikes_image_3_bikes_image_4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='condition',
            field=models.TextField(blank=True, null=True),
        ),
    ]
