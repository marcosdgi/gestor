# Generated by Django 4.2.2 on 2023-12-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0047_securitydepositdevolution'),
    ]

    operations = [
        migrations.AddField(
            model_name='securitydepositdevolution',
            name='returned_date',
            field=models.DateField(null=True),
        ),
    ]