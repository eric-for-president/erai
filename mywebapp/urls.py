from django.urls import path
from . import views
from .views import home_page_view, videos_page_view, courses_page_view, contact_page_view, downloads_page_view, registration_page_view, login_page_view, logout_view, blog_list_view, blog_create_view, blog_detail_view

urlpatterns = [
    path("", home_page_view.as_view(), name="home"),
    path("login", login_page_view, name="login"),
    path("videos", videos_page_view.as_view(), name="videos"),
    path("courses", courses_page_view.as_view(), name="courses"),
    path("contact", contact_page_view, name="contact"),
    path("downloads", downloads_page_view.as_view(), name="downloads"),
    path("register", registration_page_view, name="register"),
    path("logout", logout_view, name="logout"),
    path('blog/', blog_list_view, name='blog_list'),
    path('blog/new/', blog_create_view, name='blog_create'),
    path('blog/<int:pk>/', blog_detail_view, name='blog_detail'),
]
