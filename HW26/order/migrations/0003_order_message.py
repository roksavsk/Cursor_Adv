# Generated by Django 3.2.5 on 2021-08-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
