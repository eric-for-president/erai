from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
class home_page_view(TemplateView):
    template_name = "index.html"
    
class videos_page_view(TemplateView):
    template_name = "videos.html"

class courses_page_view(TemplateView):
    template_name = "courses.html"
    
class contact_page_view(TemplateView):
    template_name = "contact.html"
    
class downloads_page_view(TemplateView):
    template_name = "downloads.html"

# --- Registration and Login Function-Based Views ---
def registration_page_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'registration.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'registration.html')
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        auth_login(request, user)
        return redirect('home')
    return render(request, 'registration.html')

def login_page_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('home')