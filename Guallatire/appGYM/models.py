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
    nro_tarjeta = models.CharField("Número de tarjeta", max_length=16, default='0000000000000000')
    mes_expiracion = models.CharField(max_length=10,blank=True)
    año_expiracion = models.CharField(max_length=10,blank=True)
    nombre_titular =models.CharField("Nombre del titular", max_length=255, default='')
    cvv = models.CharField(max_length=4,blank=True)
    hora = models.CharField(max_length=64,blank=True)
    activo = models.BooleanField(default=False)
    sexo = models.CharField(max_length=64, blank=True)
    peso = models.CharField(max_length=64, blank=True)
    altura = models.CharField(max_length=64, blank=True)
    imc = models.CharField(max_length=64, blank=True)
    
    USERNAME_FIELD = 'user.email'

    #def clean(self):
    #    if len(self.nro_tarjeta) != 16:
    #        raise ValidationError('El número de tarjeta debe tener 16 dígitos.')
    #    
    #    if self.año_expiracion < datetime.date.today():
    #        raise ValidationError('La fecha de vencimiento debe ser posterior a la fecha actual.')

    def __str__(self):
        text = "{0},{1},{2},{3},{4},{5},{6},{7}"
        return text.format(self.user.id,self.nombre, self.apellido,self.nro_tarjeta,self.mes_expiracion,self.año_expiracion,self.cvv,self.nombre_titular)

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


