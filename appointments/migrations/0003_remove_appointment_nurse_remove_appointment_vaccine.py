# Generated by Django 4.2.7 on 2023-11-27 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_vaccineschedule_vaccine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='nurse',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='vaccine',
        ),
    ]
