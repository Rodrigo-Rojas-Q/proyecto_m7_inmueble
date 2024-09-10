from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # URL raíz
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Usa LoginView correctamente
    path('logout/', views.custom_logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('agregar-inmueble/', views.agregar_inmueble, name='agregar_inmueble'),
    path('lista-inmuebles/', views.lista_inmuebles, name='lista_inmuebles'),
    path('inmueble/<int:id>/', views.detalle_inmueble, name='detalle_inmueble'),  # Ruta para el detalle del inmueble
    path('inmueble/actualizar/<int:id>/', views.actualizar_inmueble, name='actualizar_inmueble'),
    path('inmueble/<int:id>/borrar/', views.borrar_inmueble, name='borrar_inmueble'),
    path('obtener-comunas/', views.obtener_comunas, name='obtener_comunas'),

    
    #path('inmueble/<int:id>/editar/', views.actualizar_inmueble, name='actualizar_inmueble'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)