# Generated by Django 4.2.7 on 2023-11-28 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_patient_age'),
        ('recordsapp', '0004_vaccinationrecord_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccinationrecord',
            name='nurse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nursevaccinations', to='users.nurse'),
        ),
    ]
