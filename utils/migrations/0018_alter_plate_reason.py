# Generated by Django 4.2.2 on 2023-09-21 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0017_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plate',
            name='reason',
            field=models.CharField(choices=[('repair', 'Repair'), ('rental', 'Rental'), ('storage', 'Storage'), ('other', 'Other')], max_length=50),
        ),
    ]