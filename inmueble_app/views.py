from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied

def index(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'perfil.html', {'user': request.user})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('perfil')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})

@login_required
def custom_logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def agregar_inmueble(request):
    if request.method == 'POST':
        form = AddInmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.arrendador = request.user  # Asigna el arrendador logueado
            inmueble.save()
            return redirect('lista_inmuebles')  # Redirecciona a la página de lista de inmuebles
        else:
            print(form.errors)  # Imprimir los errores en la consola
    else:
        form = AddInmuebleForm()
    
    return render(request, 'agregar_inmueble.html', {'form': form})



def lista_inmuebles(request):
    # Muestra todos los inmuebles para todos los usuarios autenticados
    user = request.user

    # Verifica si el usuario es arrendador
    if user.tipo_usuario:  # Suponiendo que este campo existe en el modelo User
        # Si es arrendador, solo muestra los inmuebles que él ha registrado
        inmuebles_list = Inmueble.objects.filter(arrendador=user)
    else:
        # Si no es arrendador, muestra todos los inmuebles (o puedes manejarlo de otra forma)
        inmuebles_list = Inmueble.objects.all()

    paginator = Paginator(inmuebles_list, 10)  # Muestra 10 inmuebles por página

    page_number = request.GET.get('page')
    inmuebles = paginator.get_page(page_number)
    return render(request, 'lista_inmuebles.html', {'inmuebles': inmuebles})

def detalle_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)  # Busca el inmueble por id
    return render(request, 'detalle_inmueble.html', {'inmueble': inmueble})

def actualizar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    
    # Verifica si el usuario es el arrendador del inmueble
    if request.user != inmueble.arrendador:
        raise PermissionDenied

    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('lista_inmuebles')
    else:
        form = InmuebleForm(instance=inmueble)

    return render(request, 'actualizar_inmueble.html', {'form': form, 'inmueble': inmueble})

def borrar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    
    # Verificar si el usuario es el arrendador del inmueble
    if request.user == inmueble.arrendador:
        inmueble.delete()
        return redirect('lista_inmuebles')  # Redirigir a la lista después de eliminar
    return redirect('detalle_inmueble', id=inmueble.id)  # Redirigir si no es el arrendador



