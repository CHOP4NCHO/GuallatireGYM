from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import UserLoginForm,UsuariosRegisterForm, Usuarios

# Create your views here.
def showLogout(request):
    contexto = {
        "mensaje":"Se ha cerrado sesión"
    }
    logout(request)
    return render(request,"login.html",contexto)
def showLogin(request):
    contexto = {
        "formLogin":UserLoginForm,
    }
    if request.method == "GET":
        logout(request)
        return render(request,"login.html",contexto)
    else:
        post_email = request.POST['email']
        post_passw = request.POST['password']

        user= authenticate(request,username=post_email, password=post_passw)
        if user == None:
            contexto["mensajeError"] = "Credenciales incorrectas!!"
            return render(request,"login.html",contexto)
        else:
            login(request,user)
            return redirect("../home/")
        
def showManageMembers(request):
    contexto = {
        "tipo":"",
        "Message": "",
        "Entrenadores": Usuarios.objects.filter(rol="Entrenador"),
        "Usuarios": User.objects.all(),
    }
    if request.method == "GET":
        return render(request, "managemembers.html",contexto)
    
    correo = request.POST['email']
    contraseña = request.POST['password']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    entrenador = request.POST['entrenador']
    rut = request.POST['rut']
    rol = request.POST['rol']
        
            
    if User.objects.filter(email=correo).exists():
        contexto["errorMessage"] = "Ya existe un usuario con ese correo!!!"
        return render(request,"createnewuser.html",contexto)
    User.objects.create_user(username=correo,email=correo,password=contraseña)
    user = User.objects.get(email=correo)
    user.usuarios = Usuarios.objects.create(
        user=user,
        nombre=nombre,
        apellido=apellido,
        entrenador=entrenador,
        rut=rut,
        rol=rol)

            
    return render(request,"managemembers.html",contexto)


def filtrarPorColumna(request):
        filtro = request.POST['filtro']  
        columna = request.POST['columna']
        match columna:
                case "sin_filtro":
                        usuarios_filtrados = Usuarios.objects.all()
                        filtro = ""
                case "nombre":
                        usuarios_filtrados= Usuarios.objects.filter(nombre__startswith=filtro)
                        ...
                case "apellido":
                        usuarios_filtrados= Usuarios.objects.filter(apellido__startswith=filtro)
                        ...
                case "rut":
                        usuarios_filtrados= Usuarios.objects.filter(rut__startswith=filtro)
                        ...
                case "rol":
                        usuarios_filtrados= Usuarios.objects.filter(rol__startswith=filtro)
        entrenadores = Usuarios.objects.filter(rol="Entrenador")                         

        return render(request, "managemembers.html",{"Usuarios":usuarios_filtrados,"Entrenadores":entrenadores,"filtro":filtro,"columna":columna})


def editMembers(request,user_id):
    contexto = {
        "tipo":"",
        "Message": "",
        "Entrenadores": Usuarios.objects.filter(rol="Entrenador"),
        "Usuarios": Usuarios.objects.all()

    }
    if request.method == "GET":
        usuario = Usuarios.objects.get(user_id = user_id)
        entrenadores = Usuarios.objects.filter(rol="Entrenador")                               # Para obtener todos los usuarios de la base de datos
        return render(request, "edicionUsuario.html",{"usuario":usuario,"Entrenadores":entrenadores})

def MembersEdited(request):
    idUsuario = request.POST['id']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    correo = request.POST['email']
    rol = request.POST['rol']
    entrenador = request.POST['entrenador']
    if (entrenador == "..."):
        entrenador = ""
    #return (HttpResponse(f"{idUsuario},{nombre},{apellido},{correo},{rol},{entrenador}"))
    usuario = Usuarios.objects.get(id = idUsuario)
    user = usuario.user

    usuario.nombre = nombre
    usuario.apellido = apellido
    user.email = correo
    user.username = correo
    usuario.rol = rol
    usuario.entrenador = entrenador
    usuario.save()
    user.save()
    messages.success(request,"Usuario editado")

    return redirect('/manageusers/')

def eliminarUsuario(request,user_id):
        usuario = Usuarios.objects.get(user_id = user_id)
        user = usuario.user
        usuario.delete()
        user.delete()
        messages.success(request,"Usuario eliminado")
        return redirect('/manageusers/')
    

        


def showHome(request):
    if request.method == "GET":
        return render(request,"home.html")
    
    

def showUserManager(request):
    return render(request, "manageusers.html")