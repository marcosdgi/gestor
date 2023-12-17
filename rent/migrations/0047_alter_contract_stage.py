# Generated by Django 4.2.2 on 2023-12-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rent", "0046_merge_20231129_1247"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="stage",
            field=models.CharField(
                choices=[
                    ("active", "Active"),
                    ("ended", "Ended"),
                    ("signed", "Signed"),
                    ("ready", "Ready to sign"),
                    ("missing", "Missing data"),
                    ("garbage", "Garbage"),
                ],
                max_length=10,
            ),
        ),
    ]
