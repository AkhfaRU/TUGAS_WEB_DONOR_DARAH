# App1/views.py
from django.shortcuts import render, redirect
from .models import Donor
from django.http import HttpResponse
import urllib.parse
from django.contrib import messages
from App1.pendaftaran import SignupForm, LoginForm
from App1.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import JadwalDonor



def home(request):
    return render(request, 'home.html')  # Sesuaikan dengan nama file template Anda

def jadwal(request):
    return render(request, 'jadwal.html')  # Sesuaikan dengan nama file template Anda

def petugas(request):
    return render(request, 'petugas.html')

def lapDonasi(request):
    return render(request, 'lapDonasi.html')  # Sesuaikan dengan nama file template Anda

def stok(request):
    return render(request, 'stok.html')  # Sesuaikan dengan nama file template Anda

def registrasi(request):
    if request.method == 'POST':
        # Menangkap data dari form
        nama = request.POST['nama']
        tanggal_lahir = request.POST['tanggal_lahir']
        no_telepon = request.POST['no_telepon']
        jenis_kelamin = request.POST['jenis_kelamin']
        golongan_darah = request.POST['golongan_darah']
        riwayat_penyakit = request.POST['riwayat_penyakit']
        alamat = request.POST['alamat']

        # Menyimpan data ke dalam database
        donor = Donor(
            nama=nama,
            tanggal_lahir=tanggal_lahir,
            no_telepon=no_telepon,
            jenis_kelamin=jenis_kelamin,
            golongan_darah=golongan_darah,
            riwayat_penyakit=riwayat_penyakit,
            alamat=alamat
        )
        donor.save()  # Simpan ke database

        return redirect('sukses')  # Arah ke halaman sukses setelah submit

    return render(request, 'registrasi.html')
    
def sukses(request):
    return render(request, 'sukses.html')


def pilih_jadwal(request):
    jadwal_list = JadwalDonor.objects.all().order_by('tanggal')
    return render(request, 'jadwal/pilih_jadwal.html', {'jadwal_list': jadwal_list})

def kirim(request):
    if request.method == 'POST':
        # Ambil data dari form
        nama = request.POST.get('nama', '').strip()
        pesan = request.POST.get('pesan', '').strip()

        if not nama or not pesan:
            # Validasi: jika nama atau pesan kosong, kembalikan error
            return HttpResponse("Nama dan pesan tidak boleh kosong.", status=400)

        # Format pesan untuk WhatsApp
        nomor_whatsapp = "6285798680711"  # Ganti dengan nomor tujuan
        pesan_final = f"{nama}\n{pesan}"
        # Encode pesan agar sesuai dengan URL
        url = f"https://wa.me/{nomor_whatsapp}?text={urllib.parse.quote(pesan_final)}"
        # Redirect ke WhatsApp
        return redirect(url)
    
    # Render form jika metode bukan POST
    return render(request, 'kirim.html')

def signup_view(request):
    if request.method == "POST":
        print("Data POST:", request.POST)  # Debugging: tampilkan data POST
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(f"Username: {username}, Email: {email}, Password: {password}")  # Debugging

        # Lanjutkan dengan logika penyimpanan seperti sebelumnya
        ...


        # Validasi input
        if not username or not email or not password:
            return render(request, "signup.html", {"error": "Semua field harus diisi!"})

        # Hash password sebelum disimpan ke database
        hashed_password = make_password(password)

        # Simpan data ke database
        try:
            user = User(username=username, email=email, password=hashed_password)
            user.save()
            return redirect("login")  # Redirect ke halaman login setelah signup berhasil
        except Exception as e:
            return render(request, "signup.html", {"error": f"Terjadi kesalahan: {str(e)}"})

    return render(request, "signup.html")

def informasi(request):
    return render(request, 'informasi.html') 

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):
                    # Set session data
                    request.session['user_id'] = user.id
                    messages.success(request, "Login successful.")
                    return redirect('informasi')
                else:
                    messages.error(request, "Invalid credentials.")
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




def dashboard(request):
    akuns = User.objects.all() 
    donors = Donor.objects.all()  # Ambil semua data dari model Donor
    return render(request, 'dashboard.html', {'akuns': akuns,'donors': donors,})


def add_donor(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        tanggal_lahir = request.POST['tanggal_lahir']
        no_telepon = request.POST['no_telepon']
        jenis_kelamin = request.POST['jenis_kelamin']
        golongan_darah = request.POST['golongan_darah']
        riwayat_penyakit = request.POST['riwayat_penyakit']
        alamat = request.POST['alamat']

        Donor.objects.create(
            nama=nama,
            tanggal_lahir=tanggal_lahir,
            no_telepon=no_telepon,
            jenis_kelamin=jenis_kelamin,
            golongan_darah=golongan_darah,
            riwayat_penyakit=riwayat_penyakit,
            alamat=alamat,
        )
        return redirect('dashboard')

    return render(request, 'add_donor.html')

def edit_donor(request, donor_id):
    donor = Donor.objects.get(id=donor_id)

    if request.method == 'POST':
        donor.nama = request.POST['nama']
        donor.tanggal_lahir = request.POST['tanggal_lahir']
        donor.no_telepon = request.POST['no_telepon']
        donor.jenis_kelamin = request.POST['jenis_kelamin']
        donor.golongan_darah = request.POST['golongan_darah']
        donor.riwayat_penyakit = request.POST['riwayat_penyakit']
        donor.alamat = request.POST['alamat']
        donor.save()
        return redirect('dashboard')

    return render(request, 'edit_donor.html', {'donor': donor})

def delete_donor(request, donor_id):
    donor = Donor.objects.get(id=donor_id)
    donor.delete()
    return redirect('dashboard')

from .models import JadwalDonor

def pilih_jadwal(request):
    jadwal_list = JadwalDonor.objects.all()
    return render(request, 'jadwal.html', {'jadwal_list': jadwal_list})

from .models import petugas

def petugass(request):
    petugass = petugas.objects.all()
    return render(request, 'petugas.html', {'petugass': petugass})