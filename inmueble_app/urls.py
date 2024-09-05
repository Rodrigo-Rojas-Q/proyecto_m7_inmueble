from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL raíz
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Usa LoginView correctamente
    path('logout/', views.custom_logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
]