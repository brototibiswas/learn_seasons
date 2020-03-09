from django import forms

from .models import Season_Blog

class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Season_Blog
        fields = [
            'season_name',
            'season_desc'
        ]


class RawBlogpostForm(forms.Form):
    title = forms.CharField()
    desc = forms.CharField() 