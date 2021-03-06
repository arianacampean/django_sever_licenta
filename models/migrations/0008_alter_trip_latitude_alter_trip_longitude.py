# Generated by Django 4.0 on 2022-04-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_remove_journey_id_trip_trip_id_journey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='latitude',
            field=models.DecimalField(decimal_places=20, max_digits=40),
        ),
        migrations.AlterField(
            model_name='trip',
            name='longitude',
            field=models.DecimalField(decimal_places=20, max_digits=40),
        ),
    ]
