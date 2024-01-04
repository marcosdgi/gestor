# Generated by Django 4.2.2 on 2024-01-03 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rent", "0053_fix_custom_migration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trailer",
            name="year",
            field=models.IntegerField(
                choices=[
                    (2000, "<2010"),
                    (2010, 2010),
                    (2011, 2011),
                    (2012, 2012),
                    (2013, 2013),
                    (2014, 2014),
                    (2015, 2015),
                    (2016, 2016),
                    (2017, 2017),
                    (2018, 2018),
                    (2019, 2019),
                    (2020, 2020),
                    (2021, 2021),
                    (2022, 2022),
                    (2023, 2023),
                    (2024, 2024),
                ],
                verbose_name="year",
            ),
        ),
    ]