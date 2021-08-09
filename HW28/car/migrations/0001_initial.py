# Generated by Django 3.2.5 on 2021-08-03 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dealer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.brand')),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_type', models.CharField(max_length=75)),
                ('population_type', models.CharField(max_length=75)),
                ('price', models.PositiveIntegerField(default=0)),
                ('fuel_type', models.CharField(max_length=75)),
                ('status', models.CharField(blank=True, choices=[('pending', 'Pending Car Sell'), ('published', 'Published'), ('sold', 'Sold'), ('archived', 'Archived')], default='pending', max_length=15)),
                ('doors', models.PositiveSmallIntegerField(default=4)),
                ('capacity', models.PositiveIntegerField()),
                ('gear_case', models.CharField(max_length=75)),
                ('number', models.CharField(max_length=15)),
                ('slug', models.SlugField(max_length=75)),
                ('sitting_place', models.PositiveSmallIntegerField(default=4)),
                ('first_registration_date', models.DateTimeField(auto_now_add=True)),
                ('engine_power', models.PositiveIntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.color')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.dealer')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car.model')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]