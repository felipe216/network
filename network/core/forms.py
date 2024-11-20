from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import Perfil
from django.core.exceptions import ValidationError


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'