# Generated by Django 4.2.7 on 2023-11-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_appointment_nurse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccineschedule',
            name='available_slots',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='vaccineschedule',
            name='capacity',
            field=models.IntegerField(default=100),
        ),
    ]
