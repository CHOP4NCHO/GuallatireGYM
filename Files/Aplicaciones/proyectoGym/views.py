from django.shortcuts import render, redirect
from .models import Usuarios
from django.contrib import messages

# Create your views here.
def manage(request):
        usuarios = Usuarios.objects.all()                                     # Para obtener todos los usuarios de la base de datos
        messages.success(request,'Usuario Ingresado')
        return render(request, "gestionMiembros.html",{"Usuarios":usuarios})
def home(request):
        usuarios = Usuarios.objects.all()                                     # Para obtener todos los usuarios de la base de datos
        messages.success(request,'Usuario Ingresado')
        return render(request, "home.html")   # Envia la lista a la siguiente vista

def mostrarLogin(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        try:
                user = Usuarios.objects.get(correo=request.POST["correo"],contraseña=request.POST["contraseña"])
                
                
        except:
                return render(request, "home.html")
        else:
            login(request, user)
            

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
        return redirect('/gestionarMiembros/')
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

        return redirect('/gestionarMiembros')
        
        

def eliminarUsuario(request,idUsuario):
        usuario = Usuarios.objects.get(idUsuario = idUsuario)
        usuario.delete()
        messages.success(request,"Usuario eliminado")
        return redirect('/')
        
        
        