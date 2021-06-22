from django.shortcuts import render,redirect
from .models import Usuario
from .forms import UsuarioForm

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

def mod_user(request):
    return render(request,'core/mod_user.html')    

def ver_user(request):
    return render(request,'core/ver_user.html')

def eliminar_user(request):
    return render(request,'core/eliminar_user.html')