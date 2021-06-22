from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(max_length=12,primary_key=True,verbose_name='Rut')
    nombres = models.CharField(max_length=50,verbose_name='Nombres')
    appaterno = models.CharField(max_length=50,verbose_name='Apellido paterno')
    apmaterno = models.CharField(max_length=50,verbose_name='Apellido materno')
    fono = models.IntegerField(verbose_name='Teléfono')
    email=models.CharField(max_length=60, verbose_name='Email')
    password=models.CharField(max_length=60, verbose_name='Contraseña')
    genero=models.CharField(max_length=6, verbose_name='Género')
    

    def __str__(self):
        return(self.rut)
    

class Boleta(models.Model):
    nro_boleta = models.IntegerField(primary_key=True,verbose_name="Número de boleta")
    total=models.IntegerField(verbose_name="Total gasto")
    fecha = models.CharField(max_length=10,verbose_name="Fecha")
    estado_pago=models.CharField(max_length=3,verbose_name="Estado de pago")
    rut=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    

    def __str__(self):
        return(self.nro_boleta) 

