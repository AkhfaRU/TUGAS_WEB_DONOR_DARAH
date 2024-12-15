from django.shortcuts import render, redirect
from django.contrib import messages
from App1.forms import SignupForm, LoginForm
from App1.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


def home(request):
    return render(request, 'home.html')  # Render your home page


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check for duplicates
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
            else:
                try:
                    # Validate password strength
                    validate_password(password)

                    # Save the user
                    user = form.save(commit=False)
                    user.password = make_password(password)
                    user.save()

                    messages.success(request, "Account created successfully.")
                    return redirect('login')
                except ValidationError as e:
                    messages.error(request, e.messages[0])  # Display password validation error
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
                    # Set session data
                    request.session['user_id'] = user.id
                    messages.success(request, "Login successful.")
                    return redirect('home')
                else:
                    messages.error(request, "Invalid credentials.")
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
