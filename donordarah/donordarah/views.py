from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Render the home page

def login_view(request):
    return render(request, 'login.html')  # Render the login page

def signup_view(request):
    return render(request, 'signup.html')  # Render the signup page
