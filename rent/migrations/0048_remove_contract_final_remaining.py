# Generated by Django 4.2.2 on 2023-12-18 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rent", "0047_contract_final_remaining_alter_contract_stage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contract",
            name="final_remaining",
        ),
    ]