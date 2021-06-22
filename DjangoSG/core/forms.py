from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Usuario, Boleta


class UsuarioForm(forms.ModelForm):

    class Meta: 
        model= Usuario
        fields = ['rut', 'nombres', 'appaterno', 'apmaterno','fono', 'email', 'password', 'genero',]
        labels ={
            'rut': 'Rut', 
            'nombres': 'Nombres', 
            'appaterno': 'Apellido paterno', 
            'apmaterno': 'Apellido materno',
            'fono': 'Teléfono', 
            'email': 'Email', 
            'password': 'Contraseña', 
            'genero': 'Género', 
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombres', 
                    'id': 'nombres'
                }
            ), 
            'appaterno': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese apellido paterno', 
                    'id': 'appaterno'
                }
            ),
            'apmaterno': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese apellido materno', 
                    'id': 'apmaterno'
                }
            ), 
            'fono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese teléfono', 
                    'id': 'fono',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese email', 
                    'id': 'email',
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese contraseña', 
                    'id': 'password',
                }
            ),
            'genero': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'genero',
                }
            ),


        }