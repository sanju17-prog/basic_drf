# Generated by Django 5.1.5 on 2025-02-12 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signal_authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='StudentSignal',
        ),
    ]
