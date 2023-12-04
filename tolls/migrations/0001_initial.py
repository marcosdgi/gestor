# Generated by Django 4.2.2 on 2023-11-24 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rent', '0045_alter_trailerplates_trailer'),
    ]

    operations = [
        migrations.CreateModel(
            name='TollDue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('stage', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], max_length=10)),
                ('invoice', models.FileField(blank=True, upload_to='toll-invoices')),
                ('created_date', models.DateField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rent.contract')),
                ('plate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rent.trailerplates')),
            ],
        ),
    ]