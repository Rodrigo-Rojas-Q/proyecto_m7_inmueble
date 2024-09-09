from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import *

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        help_text='Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.',
        validators=[
            RegexValidator(
                regex='^[\w.@+-]+$',
                message='Ingrese un nombre de usuario válido. Este valor puede contener solo letras, números y los caracteres @/./+/-/_.',
                code='invalid_username'
            ),
        ]
    )
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
        help_text='<ul>'
                  '<li>Su contraseña no puede ser muy similar a su otra información personal.</li>'
                  '<li>Su contraseña debe contener al menos 8 caracteres.</li>'
                  '<li>Su contraseña no puede ser una contraseña comúnmente utilizada.</li>'
                  '<li>Su contraseña no puede ser completamente numérica.</li>'
                  '</ul>'
    )
    password2 = forms.CharField(
        label='Confirmación de contraseña',
        widget=forms.PasswordInput,
        help_text='Ingrese la misma contraseña que antes, para verificación.'
    )
    rut = forms.CharField(label='rut')
    direccion = forms.CharField(label='Dirección')
    telefono = forms.CharField(label='Teléfono')
    tipo_usuario = forms.ChoiceField(
        label='Tipo de usuario',
        choices=[('', '---------')] + User.TIPOS_USUARIO,
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'rut', 'direccion', 'telefono', 'tipo_usuario']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    rut = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    direccion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['email', 'rut', 'direccion', 'telefono']
        labels = {
            'email': 'Correo electrónico',
            'rut': 'RUT',
            'direccion': 'Dirección',
            'telefono': 'Teléfono'
        }
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'm2_construidos', 'm2_terreno', 'numero_estacionamientos', 'numero_habitaciones','numero_banos','direccion','arrendador','id_comuna','id_region','id_tipoinmueble','precio_mensual', 'estado']  # Ajusta los campos según tu modelo
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'm2_construidos': 'Area Construida (M2)',
            'm2_terreno': 'Area de Terreno (M2)',
            'numero_estacionamientos': 'Numero de Estacionamientos',
            'numero_habitaciones': 'Numero de Habitaciones',
            'numero_banos': 'Numero de Baños',
            'direccion': 'Dirección',
            'arrendador': 'Nombre de Arrendador',
            'id_comuna': 'Comuna',
            'id_region': 'Region',
            'id_tipoinmueble': 'Tipo de Inmueble',
            'precio_mensual': 'Precio Mensual',
            'estado': 'Estado'           
        }
        
class AddInmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'm2_construidos', 'm2_terreno', 'numero_estacionamientos', 'numero_habitaciones','numero_banos','direccion','id_comuna','id_region','id_tipoinmueble','precio_mensual', 'estado']  # Ajusta los campos según tu modelo
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'm2_construidos': 'Area Construida (M2)',
            'm2_terreno': 'Area de Terreno (M2)',
            'numero_estacionamientos': 'Numero de Estacionamientos',
            'numero_habitaciones': 'Numero de Habitaciones',
            'numero_banos': 'Numero de Baños',
            'direccion': 'Dirección',
            'id_comuna': 'Comuna',
            'id_region': 'Region',
            'id_tipoinmueble': 'Tipo de Inmueble',
            'precio_mensual': 'Precio Mensual',
            'estado': 'Estado'           
        }