from rest_framework import serializers
from .models import Usuario 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Usuario
        fields = ['rut', 'nombres', 'appaterno', 'apmaterno','fono','email','password','genero']