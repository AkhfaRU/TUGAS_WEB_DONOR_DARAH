# Generated by Django 5.1.2 on 2024-12-14 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('tanggal_lahir', models.DateField()),
                ('no_telepon', models.CharField(max_length=15)),
                ('jenis_kelamin', models.CharField(max_length=10)),
                ('golongan_darah', models.CharField(max_length=5)),
                ('riwayat_penyakit', models.TextField(blank=True)),
                ('alamat', models.TextField()),
            ],
        ),
    ]
