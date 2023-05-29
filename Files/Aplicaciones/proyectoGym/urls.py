from django.urls import path 
from . import views
from .views import HomeView

urlpatterns = [
    #path('', views.home),
    path('registrarUsuario/',views.registrarUsuario),
    path('edicionUsuario/<idUsuario>',views.edicionUsuario),
    path('editarUsuario/',views.editarUsuario),
    path('eliminarUsuario/<idUsuario>',views.eliminarUsuario),
    path('gestionarMiembros/',views.manage),
    path('login/',views.showLogin),
    path('modificarTarjeta/',views.modificarTarjeta),
    path('home/', views.home),
]