# Generated by Django 4.2.13 on 2024-05-18 11:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('user_first_name', models.CharField(default='', max_length=150, null=True)),
                ('user_surname', models.CharField(default='', max_length=150, null=True)),
                ('user_contact_number', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=True)),
                ('is_verified', models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=True)),
                ('is_terms_cond_accept', models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=True)),
                ('is_staff', models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False)),
                ('is_corperate', models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False)),
                ('is_customer', models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False)),
                ('is_driver', models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
