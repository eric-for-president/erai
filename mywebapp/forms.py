from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'file']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
