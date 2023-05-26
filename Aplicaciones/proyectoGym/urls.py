from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home),
    path('registrarUsuario/',views.registrarUsuario),
    path('edicionUsuario/<idUsuario>',views.edicionUsuario),
    path('editarUsuario/',views.editarUsuario),
    path('eliminarUsuario/<idUsuario>',views.eliminarUsuario)
]