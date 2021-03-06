# Generated by Django 3.2.3 on 2021-06-22 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('appaterno', models.CharField(max_length=50, verbose_name='Apellido paterno')),
                ('apmaterno', models.CharField(max_length=50, verbose_name='Apellido materno')),
                ('fono', models.IntegerField(verbose_name='Teléfono')),
                ('email', models.CharField(max_length=60, verbose_name='Email')),
                ('password', models.CharField(max_length=60, verbose_name='Contraseña')),
                ('genero', models.CharField(max_length=6, verbose_name='Género')),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('nro_boleta', models.IntegerField(primary_key=True, serialize=False, verbose_name='Número de boleta')),
                ('total', models.IntegerField(verbose_name='Total gasto')),
                ('fecha', models.CharField(max_length=10, verbose_name='Fecha')),
                ('estado_pago', models.CharField(max_length=3, verbose_name='Estado de pago')),
                ('rut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
    ]
