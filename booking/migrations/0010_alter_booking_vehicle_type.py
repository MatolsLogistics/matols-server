# Generated by Django 4.2.13 on 2024-06-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_rename_pickup_dropoff_locations_booking_pickup_dropoff_routes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='vehicle_type',
            field=models.FloatField(blank=True, choices=[(1, '1 Ton'), (1.5, '1.5 Ton'), (2, '2 Ton'), (3, '3 Ton'), (8, '8 Ton')], default=1.0, null=True),
        ),
    ]
