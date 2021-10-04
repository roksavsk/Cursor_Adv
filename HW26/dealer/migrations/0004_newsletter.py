# Generated by Django 3.2.5 on 2021-08-03 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0003_auto_20210803_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
                'verbose_name': 'News Letter',
                'verbose_name_plural': 'News Letters',
            },
        ),
    ]