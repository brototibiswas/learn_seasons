from django import forms

from .models import Season_Blog

class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Season_Blog
        fields = [
            'season_name',
            'season_desc'
        ]


class RawSeasonPostForm(forms.Form):
    CHOICES = [
        ("WTR","Winter"), ("SMR","Summer"), ("FL","Fall"), ("SPR","Spring")
    ]

    season_name = forms.ChoiceField(
        widget = forms.Select(
            attrs = {
                "class" : "form-control"
            }
        ), choices = CHOICES
    )

    season_desc = forms.CharField(
        widget = forms.Textarea(
            attrs = { 
                    "class" : "form-control",
                    "rows" : 6,
                    "placeholder" : "Add few lines of Season description"
            }
        )
    ) 