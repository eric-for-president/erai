from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from .models import BlogPost
from .forms import BlogPostForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
class home_page_view(TemplateView):
    template_name = "index.html"
    
class videos_page_view(TemplateView):
    template_name = "videos.html"

class courses_page_view(TemplateView):
    template_name = "courses.html"
    
def contact_page_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        # You can add email/message handling here if needed
        hello_message = f"Hello {name}, thank you for contacting us!"
        return render(request, 'contact.html', {'hello_message': hello_message})
    return render(request, 'contact.html')

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
        # Send welcome email
        send_mail(
            'Welcome to Ethical Robotics and AI universe!',
            f'Hello {username},\n\nThank you for registering at Ethical Robotics and AI club. We are excited to have you on board!\n\nBest regards,\nThe ERAI Team',
            None,  # Use DEFAULT_FROM_EMAIL
            [email],
            fail_silently=True,
        )
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

def blog_list_view(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'posts': posts})

@login_required
def blog_create_view(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog_create.html', {'form': form})

def blog_detail_view(request, pk):
    post = BlogPost.objects.get(pk=pk)
    comments = post.comments.all().order_by('created_at')
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('blog_detail', pk=pk)
        else:
            return redirect('login')
    else:
        comment_form = CommentForm()
    return render(request, 'blog_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})