from django import forms
from .model import cruds

class crudFoms(forms.ModelForm):
    class Meta:
        model=cruds
        fields="__all__"
