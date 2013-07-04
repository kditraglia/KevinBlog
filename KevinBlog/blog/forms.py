from django import forms
from django.forms import ModelForm
from blog.models import Picture

class UploadForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['name', 'app_logo']
