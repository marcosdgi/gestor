# Generated by Django 4.2.2 on 2023-12-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tolls", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tolldue",
            name="invoice_number",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]