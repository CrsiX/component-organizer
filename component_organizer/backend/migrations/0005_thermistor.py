# Generated by Django 3.1.3 on 2020-11-26 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_potentiometer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thermistor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schematic_symbol_path', models.CharField(blank=True, default='', max_length=1024)),
                ('datasheet_path', models.CharField(blank=True, default='', max_length=1024)),
                ('mounting', models.CharField(choices=[('THT', 'THT'), ('SMD', 'SMD'), ('Other', 'Other')], default='THT', max_length=255)),
                ('tolerance', models.FloatField(blank=True, default=0)),
                ('max_power_dissipation', models.FloatField(blank=True, default=0)),
                ('thermistor_type', models.CharField(choices=[('NTC', 'NTC'), ('PTC', 'PTC')], default='NTC', max_length=255)),
                ('temp_min', models.FloatField(blank=True, default=0)),
                ('temp_max', models.FloatField(blank=True, default=0)),
                ('temp_switch', models.FloatField(blank=True, default=0)),
                ('custom_values', models.ManyToManyField(blank=True, to='backend.KeyValuePair')),
                ('locations', models.ManyToManyField(blank=True, to='backend.ItemLocationModel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
