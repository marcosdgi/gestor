# Generated by Django 4.2.2 on 2023-10-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0037_alter_due_lease'),
    ]

    operations = [
        migrations.AddField(
            model_name='lease',
            name='last_payment_cover',
            field=models.DateField(blank=True, null=True),
        ),
    ]