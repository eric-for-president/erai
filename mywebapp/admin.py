from django.contrib import admin
from django.contrib.admin import ModelAdmin, site
from .models import BlogPost, Comment

class BlogPostAdmin(ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')
    list_filter = ('created_at',)

class CommentAdmin(ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('post__title', 'author__username', 'content')
    list_filter = ('created_at',)

site.register(BlogPost, BlogPostAdmin)
site.register(Comment, CommentAdmin)
