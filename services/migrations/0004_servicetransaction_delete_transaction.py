# Generated by Django 4.1.2 on 2022-12-03 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
        ('services', '0003_alter_transaction_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True)),
                ('tax', models.FloatField(default=8.25)),
                ('price', models.FloatField()),
                ('quantity', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.order')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]