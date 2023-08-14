# Generated by Django 4.2.2 on 2023-08-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0009_lease_contact_name_lease_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailer',
            name='type',
            field=models.CharField(choices=[('flatbed', 'Flatbed'), ('car_hauler', 'Car Hauler'), ('3car', '3-Car Carrier'), ('mini5', 'Mini-5'), ('lowboy', 'Lowboy'), ('other', 'Other')], max_length=20),
        ),
    ]