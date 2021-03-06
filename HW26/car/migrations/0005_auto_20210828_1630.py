# Generated by Django 3.2.5 on 2021-08-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_rename_pollutant_class_car_pollutant_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='capacity',
            field=models.PositiveIntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='car',
            name='gear_case',
            field=models.CharField(blank=True, choices=[('Automatic', 'Automatic'), ('Semi-automatic', 'Semi-automatic'), ('Mechanical', 'Mechanical'), ('Robotic', 'Robotic')], default='Automatic', max_length=55),
        ),
    ]
