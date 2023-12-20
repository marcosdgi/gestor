# Generated by Django 4.2.2 on 2023-12-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0021_monthlystatistics'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='returned_security_payments',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='security_payments',
            field=models.FloatField(default=0),
        ),
    ]