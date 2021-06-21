from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request,'inicio.html')

def galeria(request):
    return render(request,'galeria.html')

def quienessomos(request):
    return render(request,'quienessomos.html')

def registro(request):
    return render(request,'registro.html')

def comentario(request):
    return render(request,'comentario.html')