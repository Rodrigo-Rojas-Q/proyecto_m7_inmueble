from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import User

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