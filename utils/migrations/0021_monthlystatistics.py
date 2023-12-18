# Generated by Django 4.2.2 on 2023-12-17 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0020_order_processing_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="MonthlyStatistics",
            fields=[
                (
                    "statistics_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="utils.statistics",
                    ),
                ),
            ],
            bases=("utils.statistics",),
        ),
    ]