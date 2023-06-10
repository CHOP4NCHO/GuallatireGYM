from django.db import models
from django.contrib.auth.hashers import * 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# Este modelo esta basado en MTV (Model, template, view)
#Model : Como se manipulan los datos de la app
#Template : Como se van a mostrar estos datos en el app
#View : Decidir donde y cuando se van a ver estos datos en la aplicacion


#ORM (Object Relational Mapping)
#ORM es para manipular la base de datos como si fuera una clase de POO

class Usuarios(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    idUsuario = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=30,blank=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    rol = models.CharField(max_length=30)
    entrenador = models.CharField(max_length=100,blank=True)
    tarjeta = models.CharField(max_length=100,blank=True)

    def __str__(self):
        text = "{0},{1},{2},{3},{4},{5}"
        return text.format(self.idUsuario,self.nombre, self.apellido,self.rol,self.entrenador,self.tarjeta)
