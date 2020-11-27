# Generated by Django 3.1.3 on 2020-11-27 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20201127_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schematic_symbol_path', models.CharField(blank=True, default='', max_length=1024)),
                ('datasheet_path', models.CharField(blank=True, default='', max_length=1024)),
                ('mounting', models.CharField(choices=[('THT', 'THT'), ('SMD', 'SMD'), ('Other', 'Other')], default='THT', max_length=255)),
                ('rated_current', models.FloatField(default=0)),
                ('trigger_characteristics', models.CharField(choices=[('superflink', 'FF'), ('flink', 'F'), ('mittelträge', 'M'), ('träge', 'T'), ('superträge', 'TT')], default='F', max_length=255)),
                ('custom_values', models.ManyToManyField(blank=True, to='backend.KeyValuePair')),
                ('locations', models.ManyToManyField(blank=True, to='backend.ItemLocationModel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
