from django import forms
from .models import Blogpost
from ckeditor.widgets import CKEditorWidget

class BlogpostForm(forms.ModelForm):
    class Meta:
        model=Blogpost
        fields='__all__'
        widgets = {
	        'title': forms.TextInput(attrs={'class': 'input','placeholder':'Title'})
        }
        