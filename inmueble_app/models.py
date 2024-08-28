from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoInmueble(models.Model):
    nombre_tipo_inmueble = models.CharField(max_length=100)

class TipoUser(models.Model):
    nombre_tipo_usuario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_tipo_usuario

class User(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    tipo_usuario = models.ForeignKey(TipoUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Region(models.Model):
    nombre_region = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_region

class Comuna(models.Model):
    nombre_comuna = models.CharField(max_length=100)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_comuna

class Inmueble(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_terreno = models.FloatField()
    numero_estacionamientos = models.IntegerField()
    numero_habitaciones = models.IntegerField()
    numero_banos = models.IntegerField()
    direccion = models.CharField(max_length=255)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    id_tipoinmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
