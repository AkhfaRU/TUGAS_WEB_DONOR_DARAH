# Generated by Django 5.1.2 on 2024-12-16 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0009_petugas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petugas',
            old_name='namaa',
            new_name='nama',
        ),
    ]