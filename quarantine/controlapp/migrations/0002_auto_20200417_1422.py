# Generated by Django 3.0.4 on 2020-04-17 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controlapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidences',
            old_name='location',
            new_name='geom',
        ),
    ]
