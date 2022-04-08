from django import forms
from django.core.validators import validate_email
from django.core import validators
from .models import etudiants

class DateInput(forms.DateInput):
    input_type = 'date'


class  FormSaveForms(forms.ModelForm):
    nom = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    prenom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_Naissance = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}))
    nni = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telephone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))


    class Meta:
        model = etudiants
        fields = ["nom", "prenom" , "date_Naissance" ,"nni", "email"  ,"telephone" ,"photo"  ]
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except:
            raise forms.ValidationError("email is not in correct format")
        return email
