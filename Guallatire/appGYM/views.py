from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime

from .models import UserLoginForm,UsuariosRegisterForm, Usuarios, PlanDeEjercicio

# Create your views here.
def showLogout(request):
    contexto = {
        "mensaje":"Se ha cerrado sesión"
    }
    logout(request)
    return redirect("../login/")
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
        if user == None or not user.is_active:
            contexto["errorMessage"] = "Credenciales incorrectas o Usuario no activo!!"
            return render(request,"login.html",contexto)
        else:
            login(request,user)
            return redirect("../home/")

def showPlanesEjercicio(request):
    contexto = {
        "Planes": PlanDeEjercicio.objects.all()       
    }
    
    return render(request,"revisarplanes.html",contexto)
    
        
def crearPlanEjercicio(request):
    contexto = {
        "Planes": PlanDeEjercicio.objects.all()      
    }
    if request.method == "GET":
        return render(request,"revisarplanes.html",contexto)
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    nivel = request.POST["nivel"]
    nuevoplan = PlanDeEjercicio.objects.create(nombre=nombre,descripcion=descripcion,nivel=nivel)
    nuevoplan.save()
    return redirect('/verplanes/')
         
def mostrarVistaEditarPlan(request, idPlan):
     plan = PlanDeEjercicio.objects.get(id =idPlan)
     contexto = {
          "plan": plan
     }
     return render(request, "editarPlan.html",contexto)

def modificarPlan(request):
    contexto = {
         "Planes": PlanDeEjercicio.objects.all()
    }
    if request.method == "GET":
        return HttpResponse("No se nada yo")
    else:
        idPlan = request.POST['idplan']
        plan = PlanDeEjercicio.objects.get(id=idPlan)
        nuevonombre = request.POST['nombre']
        nuevadesc = request.POST['descripcion']
        nuevonivel = request.POST['nivel']
        plan.nombre = nuevonombre
        plan.descripcion = nuevadesc
        plan.nivel = nuevonivel
        plan.save()
        return redirect('/verplanes/')
def eliminarPlan(request,idPlan):
     contexto = {
          "Planes" : PlanDeEjercicio.objects.all()
     }
     plan = PlanDeEjercicio.objects.get(id=idPlan)
     plan.delete()
     return redirect('/verplanes/')

def showManageMembers2(request):
    contexto = {
        "tipo":"",
        "Message": "",
        "Entrenadores": Usuarios.objects.filter(rol="Entrenador"),
        "Users": User.objects.all(),
    }
    if request.method == "GET":
        return render(request, "crearUsuario.html",contexto)
    
    correo = request.POST['email']
    contraseña = request.POST['password']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    entrenador = request.POST['entrenador']
    rut = request.POST['rut']
    rol = request.POST['rol']
    sexo = request.POST['sexo']
    imc = request.POST['imc']
    altura = request.POST['altura']
    peso = request.POST['peso']
        
            
    if User.objects.filter(email=correo).exists():
        contexto["errorMessage"] = "Ya existe un usuario con ese correo!!!"
        return render(request,"managemembers.html",contexto)
    User.objects.create_user(username=correo,email=correo,password=contraseña)
    user = User.objects.get(email=correo)
    user.usuarios = Usuarios.objects.create(
        user=user,
        nombre=nombre,
        apellido=apellido,
        entrenador=entrenador,
        rut=rut,
        rol=rol,
        sexo=sexo,
        imc=imc,
        altura=altura,
        peso=peso,
        activo=True
        )
    return render(request,"managemembers.html",contexto)


def showManageMembers(request):
    contexto = {
        "tipo":"",
        "Message": "",
        "Entrenadores": Usuarios.objects.filter(rol="Entrenador"),
        "Users": User.objects.all(),
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
    sexo = request.POST['sexo']
    imc = request.POST['imc']
    altura = request.POST['altura']
    peso = request.POST['peso']
        
            
    if User.objects.filter(email=correo).exists():
        contexto["errorMessage"] = "Ya existe un usuario con ese correo!!!"
        return render(request,"managemembers.html",contexto)
    User.objects.create_user(username=correo,email=correo,password=contraseña)
    user = User.objects.get(email=correo)
    user.usuarios = Usuarios.objects.create(
        user=user,
        nombre=nombre,
        apellido=apellido,
        entrenador=entrenador,
        rut=rut,
        rol=rol,
        sexo=sexo,
        imc=imc,
        altura=altura,
        peso=peso
        )
    return render(request,"managemembers.html",contexto)


def filtrarPorColumna(request):
        filtro = request.POST['filtro']  
        columna = request.POST['columna']
        entrenadores = Usuarios.objects.filter(rol="Entrenador")  
        listaobjusuarios = []
        match columna:
                case "sin_filtro":
                        usuarios_filtrados = User.objects.all()
                        filtro = ""
                        return render(request, "managemembers.html",{"Users":usuarios_filtrados,"Entrenadores":entrenadores,"filtro":filtro,"columna":columna})
                case "nombre":
                        usuarios_filtrados= Usuarios.objects.filter(nombre__startswith=filtro)
                        
                        for u in usuarios_filtrados:
                              listaobjusuarios.append(u.user)
                        ...
                case "apellido":
                        usuarios_filtrados= Usuarios.objects.filter(apellido__startswith=filtro)
                        
                        for u in usuarios_filtrados:
                              listaobjusuarios.append(u.user)
                        ...
                case "rut":
                        usuarios_filtrados= Usuarios.objects.filter(rut__startswith=filtro)
                        for u in usuarios_filtrados:
                              listaobjusuarios.append(u.user)
                        ...
                case "rol":
                        usuarios_filtrados= Usuarios.objects.filter(rol__startswith=filtro)
                        for u in usuarios_filtrados:
                              listaobjusuarios.append(u.user)

                               

        return render(request, "managemembers.html",{"Users":listaobjusuarios,"Entrenadores":entrenadores,"filtro":filtro,"columna":columna})


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
    estado = request.POST['estado']
    sexo = request.POST['sexo']
    imc = request.POST['imc']
    altura = request.POST['altura']
    peso = request.POST['peso']

    if (entrenador == "..."):
        entrenador = ""
    #return (HttpResponse(f"{idUsuario},{nombre},{apellido},{correo},{rol},{entrenador}"))
    usuario = Usuarios.objects.get(id = idUsuario) # obtengo el usuario
    user = usuario.user # ???

    usuario.nombre = nombre
    usuario.apellido = apellido
    user.email = correo
    user.username = correo
    usuario.rol = rol
    usuario.entrenador = entrenador
    if estado == "0":
        user.is_active = 0
    elif estado == "1":
        user.is_active = 1
    usuario.sexo = sexo
    
    print(f"peso usuario ingresado: {peso}")
    print(f"peso usuario actual: {usuario.peso}")
    print(f"estado usuario: {user.is_active}")
    if peso != '' and altura != '' and imc != '':
         usuario.peso = peso
         usuario.altura =altura
         usuario.imc = imc
         
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
    
def modificarTarjeta(request):
        tarjeta = request.POST['tarjeta']
        mesExpiracion= request.POST['mes']
        añoExpiracion = request.POST['año']
        nombre_titular = request.POST['nombreTitular']
        cvvCode = request.POST['cvv']
        id = request.POST['idTarjeta']
        usuario = Usuarios.objects.get(user_id = id)
        usuario.nro_tarjeta = tarjeta
        usuario.mes_expiracion = mesExpiracion
        usuario.año_expiracion = añoExpiracion
        usuario.nombre_titular = nombre_titular
        usuario.cvv = cvvCode
        usuario.save()
        return redirect('/manageusers/')
        


def showHome(request):
    if request.method == "GET":
        return render(request,"home.html")
    
    

def showUserManager(request):
    return render(request, "manageusers.html")

def registrarSalida(request, idUsuario):
        usuario = User.objects.get(id = idUsuario)
        usuario.usuarios.activo = 0
        usuario.usuarios.save()
        usuario.save()
        salida = datetime.now()
        entrada = datetime.fromisoformat(usuario.usuarios.hora)
        t = salida-entrada
        mensaje = 'El tiempo transcurrido fue de %s segundos' %t
        print(salida)
        print()
        print(mensaje)
        return render(request,"home.html",{"Usuarios":usuario.usuarios.nombre, "Estado":usuario.usuarios.activo, "idUsuario":usuario.id, "mensaje":mensaje})

def registrarEntrada(request, idUsuario):
        entrada = datetime.now()
        usuario = User.objects.get(id = idUsuario)
        usuario.usuarios.activo = 1
        usuario.usuarios.hora = entrada
        usuario.usuarios.save()
        usuario.save()
        print(entrada)
        return render(request,"home.html",{"Usuarios":usuario.usuarios.nombre, "Estado":usuario.usuarios.activo, "idUsuario":usuario.id})