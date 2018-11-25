from django import forms
from .models import Cat


class CatCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=15, help_text=('Name:'))
    age = forms.IntegerField(help_text=('Age:'))
    breed = forms.CharField(max_length=20, help_text=('Breed:'))
    hair_color = forms.CharField(max_length=10, help_text=('Hair color:'))

    class Meta:
        model = Cat
        fields = ('name','age','breed','hair_color', )