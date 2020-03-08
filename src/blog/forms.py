from django import forms

from .models import Blog

class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'desc'
        ]

