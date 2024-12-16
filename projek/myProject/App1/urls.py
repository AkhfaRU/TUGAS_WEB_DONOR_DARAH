# App1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrasi/', views.registrasi, name='registrasi'),  # Halaman registrasi
    path('sukses/', views.sukses, name='sukses'),    # Halaman sukses
    path('kirim/', views.kirim, name='kirim'),
    path('signup/', views.signup_view, name='signup'),
    path('berhasil/', views.signup_view, name='berhasil'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-donor/', views.add_donor, name='add_donor'),  # Create
    path('edit-donor/<int:donor_id>/', views.edit_donor, name='edit_donor'),  # Update
    path('delete-donor/<int:donor_id>/', views.delete_donor, name='delete_donor'),  # Delete
    path('informasi/', views.informasi, name='informasi'),
    path('jadwal/', views.pilih_jadwal, name='jadwal'),
    path('petugas/', views.petugass, name='petugas'),
    path('stok/', views.stok, name='stok'),
    path('lapDonasi/', views.lapDonasi, name='lapDonasi'),

]
