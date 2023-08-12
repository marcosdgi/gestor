# Generated by Django 4.2.2 on 2023-07-30 01:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0015_order_invoice_data_order_vin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='badge',
        ),
        migrations.AddField(
            model_name='order',
            name='position',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)]),
        ),
    ]