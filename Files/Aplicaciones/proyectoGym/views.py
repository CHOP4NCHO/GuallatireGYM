from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Usuarios
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import * 
from itertools import cycle

# Create your views here.
def home(request):           
        print("xd")                        # Para obtener todos los usuarios de la base de datos
        return render(request, "home.html")                                 # Envia la lista a la siguiente vista
# Para visualizar el home
class HomeView(View):
        def __init__(self,nombre):
                self.nombre = nombre
        def retorno(self,request):
                return render(request, 'home.html', {"Usuarios":self.nombre})
                
def manage(request):
        usuarios = Usuarios.objects.all()  
        entrenadores = Usuarios.objects.filter(rol="Entrenador")                           # Para obtener todos los usuarios de la base de datos
        return render(request, "gestionMiembros.html",{"Usuarios":usuarios,"Entrenadores":entrenadores})

def showLogin(request):
        if request.method == "GET":
                return render(request,"login.html")
                
        correo = request.POST['correo']
        contraseña = request.POST['contraseña'] 
        if not User.objects.filter(email=correo).exists():
                message = "Credenciales incorrectas, intente nuevamente"
                return render(request,"login.html",{"Mensaje":message})
        usuario = User.objects.get(email=correo)
        
        if (check_password(contraseña,usuario.contraseña)):
                if (usuario.rol == "Cliente"):
                        USER = usuario
                        return HomeView(USER.nombre).retorno(request)
                elif (usuario.rol == "Entrenador"):
                        nombreEntrenador = usuario.nombre
                        clientes = Usuarios.objects.filter(entrenador = nombreEntrenador)
                        return render(request,"clientesEntrenador.html",{"Clientes":clientes})
                elif (usuario.rol == "Administrador"):
                        usuarios = Usuarios.objects.all()
                        return render(request,"gestionMiembros.html",{"Usuarios":usuarios,"Entrenadores":Usuarios.objects.filter(rol="Entrenador")})
                print("No va a ninguna parte")
        return redirect('/')
                
               

def registrarUsuario(request):
        rut=request.POST['rut']
        if not verificarRut(rut):
                message = "SU RUT ES DE MENTIRA"
                return render(request,'gestionMiembros.html',{"Usuarios":Usuarios.objects.all(),"Entrenadores":Usuarios.objects.filter(rol="Entrenador"),"Message":message,"tipo":"warning"})
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['email']
        if User.objects.filter(email=correo).exists():
                message = "Ya existe el correo!!!"
                return render(request,'gestionMiembros.html',{"Usuarios":Usuarios.objects.all(),"Entrenadores":Usuarios.objects.filter(rol="Entrenador"),"Message":message,"tipo":"warning"})

        contraseña= request.POST['contraseña']
        contraseña =  make_password(contraseña)
        rol = request.POST['rol']
        try:
                entrenador = request.POST['entrenador']
        except MultiValueDictKeyError:
                entrenador = ""
        if(checkBlank([nombre,apellido,correo,contraseña,rol])):
               messages.success(request,'Algun campo esta mal escrito')  
        else:
                ####AQUI
                messages.success(request,'Usuario Ingresado')
        return redirect('/gestionarMiembros/')

def edicionUsuario(request,idUsuario):
        usuario = Usuarios.objects.get(idUsuario = idUsuario)
        entrenadores = Usuarios.objects.filter(rol="Entrenador")                               # Para obtener todos los usuarios de la base de datos
        return render(request, "edicionUsuario.html",{"usuario":usuario,"Entrenadores":entrenadores})
      

    
def editarUsuario(request):
        idUsuario = request.POST['id']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        rol = request.POST['rol']
        entrenador = request.POST['entrenador']
        if (entrenador == "..."):
                entrenador = ""
        usuario = Usuarios.objects.get(idUsuario = idUsuario)

        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.correo = correo
        usuario.rol = rol
        usuario.entrenador = entrenador
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
@csrf_protect
def modificarTarjeta(request):
        tarjeta = request.POST['tarjeta']
        id = request.POST['idTarjeta']
        usuario = Usuarios.objects.get(idUsuario = id)
        usuario.tarjeta = tarjeta
        usuario.save()
        return redirect('/gestionarMiembros/')

def verificarRut(rut):
        rut = rut.upper();
        rut = rut.replace("-","").replace(".","")
        aux = rut[:-1]
        dv = rut[-1:]
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido,factors))
        res = (-s)%11        
        if str(res) == dv:
                return True
        elif dv=="K" and res==10:
                return True
        else:
                return False
