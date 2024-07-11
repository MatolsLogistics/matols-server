# Generated by Django 4.2.13 on 2024-07-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0003_contactus_respond'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='respond',
        ),
        migrations.AddField(
            model_name='contactus',
            name='message_response',
            field=models.TextField(blank=True, default='', max_length=2000, null=True),
        ),
    ]