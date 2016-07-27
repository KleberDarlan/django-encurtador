from django import forms

from .models import Url


class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = (
            'full_url',
        )
        widgets = {
            'full_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL'})
        }
