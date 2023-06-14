from django.db import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import *
from django import forms
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    password = forms.CharField(max_length=256,widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': ''}))

    class Meta:
        model = User
        fields = ['email','password']
        help_texts = {k:"" for k in fields}



class Usuarios(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    rut = models.CharField(max_length=30,blank=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    rol = models.CharField(max_length=30)
    entrenador = models.CharField(max_length=100,blank=True)
    
    USERNAME_FIELD = 'user.email'

    nro_tarjeta = models.CharField("número de tarjeta", max_length=16, default='0000000000000000')
    fecha_exp = models.DateField("Fecha de vencimiento", default=datetime.date(2024, 1,2))
    nombre_titular =models.CharField("Nombre del titular", max_length=255, default='')
    activo = models.BooleanField(default=True)

    def clean(self):
        if len(self.nro_tarjeta) != 16:
            raise ValidationError('El número de tarjeta debe tener 16 dígitos.')
        
        if self.fecha_exp < datetime.date.today():
            raise ValidationError('La fecha de vencimiento debe ser posterior a la fecha actual.')

    def __str__(self):
        text = "{0},{1},{2},{3},{4},{5},{6}"
        return text.format(self.nombre, self.apellido,self.rol,self.entrenador,self.nro_tarjeta, self.fecha_exp, self.nombre_titular)

class UsuariosRegisterForm(forms.ModelForm):
  nombre = forms.CharField(max_length=64)
  apellido = forms.CharField(max_length=64)
  rut = models.CharField(max_length=30,blank=True)
  entrenador = models.CharField(max_length=100,blank=True)
  
  class Meta:
    model = Usuarios
    fields = ['nombre','apellido','rut','entrenador']
    help_texts = {
      k:"" for k in fields
    }

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','password']
        help_texts = {k:"" for k in fields}


