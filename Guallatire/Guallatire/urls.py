"""
URL configuration for Guallatire project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appGYM import views

urlpatterns = [
    path('',views.showLogin),
    path('admin/', admin.site.urls),
    path('home/',views.showHome),
    path('login/',views.showLogin),
    path('manageusers/',views.showManageMembers),
    path('manageusers/crearUsuario/', views.showManageMembers2),
    path('logout/',views.showLogout),
    path('edicionUsuario/<user_id>',views.editMembers),
    path('UsuarioEditado/',views.MembersEdited),
    path('eliminarUsuario/<user_id>',views.eliminarUsuario),
    path('filtrarPorColumna/',views.filtrarPorColumna),
    path('modificarTarjeta/',views.modificarTarjeta),
    path('registrarEntrada/<idUsuario>',views.registrarEntrada),
    path('registrarSalida/<idUsuario>',views.registrarSalida),
    path('verplanes/',views.showPlanesEjercicio),
    path('verplanes/mostrarEditarPlan/<idPlan>',views.mostrarVistaEditarPlan),
    path('editarPlan/',views.modificarPlan),
    path('crearPlan/',views.crearPlanEjercicio),
    path('verplanes/eliminarPlan/<idPlan>',views.eliminarPlan)
]
