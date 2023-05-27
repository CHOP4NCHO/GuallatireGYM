from django.shortcuts import render, redirect
from .models import Usuarios
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your views here.
def home(request):
        usuarios = Usuarios.objects.all()                                     # Para obtener todos los usuarios de la base de datos
        return render(request, "login.html")                                   # Envia la lista a la siguiente vista

def manage(request):
        usuarios = Usuarios.objects.all()                                     # Para obtener todos los usuarios de la base de datos
        return render(request, "gestionMiembros.html",{"Usuarios":usuarios})

def showLogin(request):
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']
        if request.method == "GET":
                return render(request, "home.html")
        else:
                try:
                        usuario = Usuarios.objects.get(correo=correo,contraseña=contraseña)
                except:
                        return render(request, "home.html")
                else:
                        print("login")

def signup(request):
        if (request.method == 'GET'):
                return render(request, 'signup.html')
        else:
                if request.POST['contraseña1'] == request.POST['contraseña2']:
                        #VERIFICAR Y REGISTRAR LA INFORMACION QUE TIENE UN USUARIO 
                        usuario = User.objects.create_user(username=request.POST['correo'], password=request.POST['contraseña'])
                        login(request,usuario)
                        #return render(request, 'home.html')
                        ...

def registrarUsuario(request):
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        contraseña= request.POST['contraseña']
        rol = request.POST['rol']
        if(checkBlank([nombre,apellido,correo,contraseña,rol])):
               messages.success(request,'Algun campo esta mal escroto')  
        else:
                usuario = Usuarios.objects.create(
                nombre = nombre,
                apelllido = apellido,
                contraseña = contraseña,
                correo = correo,
                rol = rol    
        )
                messages.success(request,'Usuario Ingresado')
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

        return redirect('/gestionarMiembros/')
        
        

def eliminarUsuario(request,idUsuario):
        usuario = Usuarios.objects.get(idUsuario = idUsuario)
        usuario.delete()
        messages.success(request,"Usuario eliminado")
        return redirect('/gestionarMiembros/')
        
def checkBlank(info=[]):
        blank = False
        for i in info:
                if (i == "" or i == "Selecione un rol"):
                        blank = True
                else:
                        return blank
        
        
        