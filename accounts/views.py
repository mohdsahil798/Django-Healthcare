from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import logout

# accounts/views.py
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        # Use 'email' instead of 'username'
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print(f"Login attempt - Email: {email}, Password: {password}")
        
        # Authenticate using email
        user = authenticate(request, email=email, password=password)
        
        print(f"Authenticated user: {user}")
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            print("Authentication failed")
            return render(request, 'accounts/login.html', {
                'error': 'Invalid email or password'
            })
    return render(request, 'accounts/login.html')

@login_required
def dashboard(request):
    user = request.user
    context = {
        'user': user,
        'user_type': user.get_user_type_display()
    }
    return render(request, 'accounts/dashboard.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')