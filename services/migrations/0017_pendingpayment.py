# Generated by Django 4.1.5 on 2023-03-31 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_associated_membership_company_membership'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0016_remove_payment_exclusive_payment_extra_charge'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.associated')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]