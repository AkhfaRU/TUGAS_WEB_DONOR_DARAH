from django import forms
from .models import Donor, User
from django.contrib.auth.password_validation import validate_password

# ini buat form 
class PendaftaranForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['nama', 'tanggal_lahir', 'no_telepon', 'jenis_kelamin', 'golongan_darah', 'riwayat_penyakit', 'alamat']


#ini buat login & signup
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password]) # type: ignore
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)