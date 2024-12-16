# Generated by Django 5.1.2 on 2024-12-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0005_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='JadwalDonor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lokasi', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
                ('kapasitas', models.PositiveIntegerField()),
                ('jam_operasional', models.CharField(default='08:00-15:00', editable=False, max_length=50)),
                ('tanggal', models.DateField()),
            ],
            options={
                'unique_together': {('lokasi', 'tanggal')},
            },
        ),
    ]