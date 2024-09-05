from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(TipoInmueble)
class TipoInmuebleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_tipo_inmueble')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'rut', 'direccion', 'telefono', 'tipo_usuario')
    search_fields = ('username', 'rut')

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_region')

@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_comuna', 'id_region')

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'arrendador', 'id_comuna', 'id_region', 'id_tipoinmueble', 'precio_mensual', 'estado')
    list_filter = ('id_comuna', 'id_region', 'estado')
    search_fields = ('nombre', 'arrendador__username')

@admin.register(SolicitudArriendo)
class SolicitudArriendoAdmin(admin.ModelAdmin):
    list_display = ('arrendatario', 'inmueble', 'fecha_solicitud', 'estado')
    list_filter = ('estado', 'fecha_solicitud')
    search_fields = ('arrendatario__username', 'inmueble__nombre')