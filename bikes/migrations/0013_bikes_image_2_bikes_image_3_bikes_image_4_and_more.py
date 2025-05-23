# Generated by Django 5.1.7 on 2025-05-08 16:30

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0012_remove_bikes_image_2_remove_bikes_image_3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='bike_image/'),
        ),
        migrations.AddField(
            model_name='bikes',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='bike_image/'),
        ),
        migrations.AddField(
            model_name='bikes',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='bike_image/'),
        ),
        migrations.AlterField(
            model_name='bikes',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=Decimal('0.0'), max_digits=2),
        ),
    ]
