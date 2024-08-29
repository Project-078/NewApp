from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            # auth.login(request, user)  # Uncomment if you want to log in the user after registration
            return redirect('login')  # Ensure 'lgn' is the correct URL name for the login page
    else:
        return render(request, 'account/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')

        else:
            return render(request, 'account/login.html', {'error': 'Invalid username or password'})
    return render(request, 'account/login.html')

def index(request):
    return render(request, 'account/index.html')