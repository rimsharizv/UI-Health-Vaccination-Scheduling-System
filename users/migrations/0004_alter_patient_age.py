# Generated by Django 4.2.7 on 2023-11-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_nurse_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
