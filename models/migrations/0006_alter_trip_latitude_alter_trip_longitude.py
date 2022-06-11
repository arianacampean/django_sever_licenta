# Generated by Django 4.0 on 2022-04-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_alter_trip_latitude_alter_trip_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='trip',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
    ]