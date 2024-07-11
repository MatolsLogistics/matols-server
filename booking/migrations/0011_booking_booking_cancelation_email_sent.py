# Generated by Django 4.2.13 on 2024-07-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_booking_vehicle_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_cancelation_email_sent',
            field=models.BooleanField(choices=[(False, 'NO'), (True, 'YES')], default=False),
        ),
    ]