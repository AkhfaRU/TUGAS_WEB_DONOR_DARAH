# App1/models.py
from django.db import models
from datetime import date, timedelta



# ini buat form 
class Donor(models.Model):
    nama = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    no_telepon = models.CharField(max_length=15)
    jenis_kelamin = models.CharField(max_length=10)
    golongan_darah = models.CharField(max_length=5)
    riwayat_penyakit = models.TextField(blank=True)
    alamat = models.TextField()

    def __str__(self):
        return self.nama

    class Meta:
        db_table = "pengguna"  # Menentukan nama tabel di database

# ini buat login & signup
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Enkripsi dilakukan sebelum penyimpanan

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = "akun"


class JadwalDonor(models.Model):
    lokasi = models.CharField(max_length=100)  # Nama lokasi
    alamat = models.TextField()  # Alamat lokasi
    kapasitas = models.PositiveIntegerField()  # Kapasitas lokasi
    jam_operasional = models.CharField(max_length=50, default="08:00-15:00", editable=False)  # Otomatis
    tanggal = models.DateField()  # Tanggal donor

    def __str__(self):
        return self.lokasi

    class Meta:
        db_table = "jadwaldonor"  

class petugas(models.Model):
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100) 
    notelp = models.CharField(max_length=15)
    tanggal = models.DateField()  

    def __str__(self):
        return self.nama

    class Meta:
        db_table = "petugas"

