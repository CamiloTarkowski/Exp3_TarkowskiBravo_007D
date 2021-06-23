from django.shortcuts import render,redirect
from .models import Usuario
from .forms import UsuarioForm
from django.views.decorators import csrf
from rest_framework.serializers import Serializer




# Create your views here.


def inicio(request):
    return render(request,'inicio.html')

def galeria(request):
    return render(request,'galeria.html')

def crear_user(request):
    if request.method=='POST': 
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('inicio')
    else:
        usuario_form= UsuarioForm()
    return render(request, 'core/crear_user.html', {'usuario_form': usuario_form})

def mod_user(request,id):
    usuario = Usuario.objects.get(rut=id)

    datos ={
        'form': UsuarioForm(instance=usuario)
    }
    if request.method == 'POST': 
        formulario = UsuarioForm(data=request.POST, instance = usuario)
        if formulario.is_valid: 
            formulario.save()           
            return redirect('inicio')
    return render(request, 'core/mod_user', datos)

def eliminar_user(request,id):
    usuario = Usuario.objects.get(rut=id)
    usuario.delete()
    return redirect('ver_user')
   

def ver_user(request):
    usuarios = Usuario.objects.all()

    return render(request, 'core/ver_user.html', context={'usuarios':usuarios})
