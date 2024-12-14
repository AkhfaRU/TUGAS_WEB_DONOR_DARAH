from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Render your home page

def login_view(request):
    return render(request, 'login.html')  # Render your login page

def signup_view(request):
    return render(request, 'signup.html')  # Render your signup page

