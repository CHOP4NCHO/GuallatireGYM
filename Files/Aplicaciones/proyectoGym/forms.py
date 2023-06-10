from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField(required=True)
  password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ['email','password']
    help_texts = {
      k:"" for k in fields
    }

class UsuarioRegisterForm(forms.ModelForm):
  nombre = forms.CharField(label="Nombre")
  apellido = forms.CharField(label="Apellido", widget=forms.PasswordInput)
  rut = forms.CharField(label="RUT")
  rol = forms.Select(choices=["Cliente","Entrenador"])
  

  class Meta:
    model = Usuarios
    fields = ['nombre','apellido','rut','rol']
    help_texts = {
      k:"" for k in fields
    }

