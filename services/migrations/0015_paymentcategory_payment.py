# Generated by Django 4.1.5 on 2023-03-25 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0008_order_equipment_type'),
        ('services', '0014_servicepicture'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('icon', models.ImageField(blank=True, upload_to='images/icons')),
                ('extra_charge', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('exclusive', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.paymentcategory')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_payment', to='utils.order')),
            ],
        ),
    ]