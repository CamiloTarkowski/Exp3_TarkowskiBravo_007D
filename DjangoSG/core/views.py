from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request,'inicio.html')

def galeria(request):
    return render(request,'galeria.html')

def crear_user(request):
    return render(request,'core/crear_user.html')

def mod_user(request):
    return render(request,'core/mod_user.html')    

def ver_user(request):
    return render(request,'core/ver_user.html')

def eliminar_user(request):
    return render(request,'core/eliminar_user.html')