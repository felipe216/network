from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import Perfil
from django.core.exceptions import ValidationError


class PerfilForm(forms.ModelForm):
    nome = forms.CharField(max_length=100)
    foto = forms.ImageField(required=False)
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    sexo = forms.ChoiceField(choices=Perfil.Sexo.CHOICES)
    cidade = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=100)
    ocupacao = forms.CharField(max_length=100)
    user = forms.HiddenInput()
    class Meta:
        model = Perfil
        fields = ["nome", "foto", "data_nascimento", "sexo", "cidade", "estado", "pais", "ocupacao"]