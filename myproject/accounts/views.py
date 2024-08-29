from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.method  == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            errors = "Invalid Credentials!."

            return render(request, 'login.html', {'errors': errors, 'username': username})
    else :
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        # first_name = request.POST.get('first_name')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        errors = {}

        if password1 != password2:
            errors['password2'] = "Passwords do not match."
        
        if User.objects.filter(username=username).exists():
            errors['username'] = "Username already taken."
        
        if User.objects.filter(email=email).exists():
            errors['email'] = "Email is already in use."

        if not errors:  # No errors, proceed with user creation
            user = User.objects.create_user(
                username=username,
                password=password1,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            messages.success(request, f'Account created for {username}!')
            print(f'user {username} created successfully!\n')
            return redirect('login')

        # If errors exist, pass them to the template
        return render(request, 'register.html', {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'errors': errors
        })
    
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
