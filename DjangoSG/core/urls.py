from django.urls import path
from .views import inicio, galeria,crear_user,mod_user,ver_user,eliminar_user


urlpatterns=[
    path('',inicio, name="inicio"),
    path('galeria/',galeria, name="galeria"),
    path('crear_usuario/',crear_user,name="crear_user"),
    path('mod_usuario/',mod_user,name="mod_user"),
    path('ver_usuario/',ver_user,name="ver_user"),
    path('eliminar_usuario/',eliminar_user,name="eliminar_user"),
    
]