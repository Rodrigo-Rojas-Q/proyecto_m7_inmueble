from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.

class TipoInmueble(models.Model):
    nombre_tipo_inmueble = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_tipo_inmueble

class User(AbstractUser):
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    TIPOS_USUARIO = [
        ('ARRENDATARIO', 'Arrendatario'),
        ('ARRENDADOR', 'Arrendador'),
    ]
    tipo_usuario = models.CharField(max_length=12, choices=TIPOS_USUARIO)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='usuario_set',
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='usuario_set',
        related_query_name='usuario',
    )
    
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
    arrendador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='propiedades')
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    id_tipoinmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE, related_name='inmuebles')
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    imagen = models.ImageField(upload_to='inmuebles/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
            while Inmueble.objects.filter(slug=self.slug).exists():
                self.slug = slugify(f"{self.nombre}-{self.pk}")
        super(Inmueble, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class SolicitudArriendo(models.Model):
    arrendatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitudes')
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('ACEPTADA', 'Aceptada'),
        ('RECHAZADA', 'Rechazada'),
    ]
    estado = models.CharField(max_length=10, choices=ESTADOS, default='PENDIENTE')