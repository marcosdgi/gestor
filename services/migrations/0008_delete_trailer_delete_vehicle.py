# Generated by Django 4.1.2 on 2022-12-24 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_trailer_vehicle'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Trailer',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]