from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms import SignupForm, LoginForm
from app.models import User
from django.contrib.auth.hashers import make_password, check_password

def home(request):
    return render(request, 'home.html')  # Render your home page

def login_view(request):
    return render(request, 'login.html')  # Render your login page

def signup_view(request):
    return render(request, 'signup.html')  # Render your signup page


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                messages.error(request, "Email already exists.")
            else:
                user = form.save(commit=False)
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                messages.success(request, "Account created successfully.")
                return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):
                    messages.success(request, "Login successful.")
                    # Simpan data sesi jika diperlukan
                    request.session['user_id'] = user.id
                    return redirect('home')
                else:
                    messages.error(request, "Invalid credentials.")
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
