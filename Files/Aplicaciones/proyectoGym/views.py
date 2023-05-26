from django.shortcuts import render, redirect
from .models import Usuarios
from django.contrib import messages

# Create your views here.
def home(request):
        usuarios = Usuarios.objects.all()                                     # Para obtener todos los usuarios de la base de datos
        messages.success(request,'Usuario Ingresado')
        return render(request, "gestionMiembros.html",{"Usuarios":usuarios})  # Envia la lista a la siguiente vista

def registrarUsuario(request):
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        contraseña= request.POST['contraseña']
        rol = request.POST['rol']

        usuario = Usuarios.objects.create(
                nombre = nombre,
                apelllido = apellido,
                contraseña = contraseña,
                correo = correo,
                rol = rol    
        )
        return redirect('/')
def edicionUsuario(request,idUsuario):
        usuario = Usuarios.objects.get(idUsuario = idUsuario)
        return render(request, "edicionUsuario.html",{"usuario":usuario})
    
def editarUsuario(request):
        idUsuario = request.POST['id']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        contraseña= request.POST['contraseña']
        rol = request.POST['rol']

        usuario = Usuarios.objects.get(idUsuario = idUsuario)

        usuario.nombre = nombre
        usuario.apelllido = apellido
        usuario.correo = correo
        usuario.contraseña = contraseña
        usuario.rol = rol 
        usuario.save()
        messages.success(request,"Usuario editado")

        return redirect('/')
        
        

def eliminarUsuario(request,idUsuario):
        usuario = Usuarios.objects.get(idUsuario = idUsuario)
        usuario.delete()
        messages.success(request,"Usuario eliminado")
        return redirect('/')
        
        
        