# Generated by Django 4.2.2 on 2023-11-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0023_service_internal_service_marketing_service_tire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/expenses'),
        ),
        migrations.AlterField(
            model_name='servicepicture',
            name='image',
            field=models.ImageField(upload_to='images/services'),
        ),
    ]
