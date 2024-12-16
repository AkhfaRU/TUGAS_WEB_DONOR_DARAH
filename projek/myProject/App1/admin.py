# App1/admin.py
from django.contrib import admin
from .models import Donor  # Mengimpor model Donor
from django.contrib import admin
from .models import JadwalDonor
from .models import petugas

admin.site.register(Donor)


@admin.register(JadwalDonor)
class JadwalDonor(admin.ModelAdmin):
    list_display = ('lokasi', 'tanggal', 'kapasitas')  # Sesuaikan field Anda
    search_fields = ('lokasi',)

@admin.register(petugas)
class petugas(admin.ModelAdmin):
    list_display = ('nama', 'jabatan', 'notelp', 'tanggal')  # Sesuaikan field Anda
    search_fields = ('nama',)