from django.shortcuts import render, redirect
from .models import Usuarios
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def home(request):
        usuarios = Usuarios.objects.all()                                     # Para obtener todos los usuarios de la base de datos
        return render(request, "login.html")                                   # Envia la lista a la siguiente vista

def manage(request):
        usuarios = Usuarios.objects.all()  
        entrenadores = Usuarios.objects.filter(rol="Entrenador")                               # Para obtener todos los usuarios de la base de datos
        return render(request, "gestionMiembros.html",{"Usuarios":usuarios,"Entrenadores":entrenadores})

def showLogin(request):
        print("Function ShowLogin")
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']
        if request.method == "GET":
                print("Porque este wea vino en formato GET?")
        else:
                print("Este metodo de formulario es POST")
                try:         
                        usuario = Usuarios.objects.get(correo=correo,contraseña=contraseña)
                        print(usuario)
                        if (usuario.rol == "Cliente"):
                                return render(request,'home.html',{"usuario":usuario})
                        elif (usuario.rol == "Entrenador"):
                                usuarios = Usuarios.objects.all()
                                return render(request,'gestionMiembros.html',{"Usuarios":usuarios}) 
                except:
                        messages.error(request,"Este usuario no existe")
                
        return redirect('/')
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
        rut=request.POST['rut']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        contraseña= request.POST['contraseña']
        rol = request.POST['rol']
        try:
                entrenador = request.POST['entrenador']
        except MultiValueDictKeyError:
                entrenador = ""
        if(checkBlank([nombre,apellido,correo,contraseña,rol])):
               messages.success(request,'Algun campo esta mal escroto')  
        else:
                usuario = Usuarios.objects.create(
                rut = rut,
                nombre = nombre,
                apellido = apellido,
                contraseña = contraseña,
                correo = correo,
                rol = rol,
                entrenador = entrenador,
                activo = True
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
        usuario.apellido = apellido
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