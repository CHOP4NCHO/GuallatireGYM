from django.db import models
from django.contrib.auth.hashers import * 
from django.core.exceptions import ValidationError
import datetime
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
        text = "{0},{1},{2},{3},{4},{5},{6},{7}, {8}, {9}"
        return text.format(self.idUsuario,self.nombre, self.apellido,self.contraseña,self.correo,self.rol,self.entrenador,self.nro_tarjeta, self.fecha_exp, self.nombre_titular)
        