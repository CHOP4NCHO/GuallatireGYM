from django.db import models
from django.contrib.auth.hashers import * 
# Create your models here.

# Este modelo esta basado en MTV (Model, template, view)
#Model : Como se manipulan los datos de la app
#Template : Como se van a mostrar estos datos en el app
#View : Decidir donde y cuando se van a ver estos datos en la aplicacion


#ORM (Object Relational Mapping)
#ORM es para manipular la base de datos como si fuera una clase de POO

class Usuarios(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=30,blank=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=40)
    correo = models.CharField(max_length=100)
    rol = models.CharField(max_length=30)
    entrenador = models.CharField(max_length=100,blank=True)
    tarjeta = models.CharField(max_length=100,blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        text = "{0},{1},{2},{3},{4},{5},{6},{7}"
        return text.format(self.idUsuario,self.nombre, self.apellido,self.contraseña,self.correo,self.rol,self.entrenador,self.tarjeta)
        