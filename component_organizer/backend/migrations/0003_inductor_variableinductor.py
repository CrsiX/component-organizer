# Generated by Django 3.1.3 on 2020-11-29 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_wire'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariableInductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schematic_symbol_path', models.CharField(blank=True, default='', max_length=1024)),
                ('datasheet_path', models.CharField(blank=True, default='', max_length=1024)),
                ('mounting', models.CharField(choices=[('THT', 'THT'), ('SMD', 'SMD'), ('Other', 'Other')], default='THT', max_length=255)),
                ('min_inductance', models.FloatField(default=0)),
                ('max_inductance', models.FloatField(default=0)),
                ('core_material', models.CharField(choices=[('air', 'air'), ('iron', 'iron'), ('ferrite', 'ferrite')], default='air', max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.category')),
                ('custom_values', models.ManyToManyField(blank=True, to='backend.KeyValuePair')),
                ('locations', models.ManyToManyField(blank=True, to='backend.ItemLocationModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Inductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schematic_symbol_path', models.CharField(blank=True, default='', max_length=1024)),
                ('datasheet_path', models.CharField(blank=True, default='', max_length=1024)),
                ('mounting', models.CharField(choices=[('THT', 'THT'), ('SMD', 'SMD'), ('Other', 'Other')], default='THT', max_length=255)),
                ('inductance', models.FloatField(default=0)),
                ('core_material', models.CharField(choices=[('air', 'air'), ('iron', 'iron'), ('ferrite', 'ferrite')], default='air', max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.category')),
                ('custom_values', models.ManyToManyField(blank=True, to='backend.KeyValuePair')),
                ('locations', models.ManyToManyField(blank=True, to='backend.ItemLocationModel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]