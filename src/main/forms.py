from django import forms
from .models import Blogpost

class BlogpostForm(forms.ModelForm):
    class Meta:
        model=Blogpost
        fields='__all__'
        widgets = {
	        'title': forms.TextInput(attrs={'class': 'input','placeholder':'Title'})
        }
        