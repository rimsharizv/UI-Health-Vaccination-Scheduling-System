# Generated by Django 4.2.7 on 2023-11-28 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0009_nurseschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurseschedule',
            name='status',
            field=models.CharField(default='Pending', max_length=255),
        ),
    ]
