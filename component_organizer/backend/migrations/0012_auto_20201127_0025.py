# Generated by Django 3.1.3 on 2020-11-27 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20201127_0005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemlocationmodel',
            old_name='number',
            new_name='amount',
        ),
    ]