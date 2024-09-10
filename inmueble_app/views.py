from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

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
        form = AddInmuebleForm(request.POST, request.FILES)  # Agrega request.FILES para manejar imágenes
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.arrendador = request.user  # Asigna el arrendador logueado
            inmueble.save()
            return redirect('lista_inmuebles')  # Redirecciona a la lista de inmuebles
        else:
            print(form.errors)  # Imprimir los errores en la consola
    else:
        form = AddInmuebleForm()

    return render(request, 'agregar_inmueble.html', {'form': form})



def lista_inmuebles(request):
    user = request.user

    # Obtener todas las regiones y comunas
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()

    # Definir la lista de inmuebles desde el principio
    inmuebles_list = Inmueble.objects.all()

    # Obtener los filtros desde los parámetros GET
    comuna_id = request.GET.get('comuna')
    region_id = request.GET.get('region')

    # Filtrar por comuna y región si están seleccionadas
    if comuna_id:
        inmuebles_list = inmuebles_list.filter(id_comuna=comuna_id)
    if region_id:
        inmuebles_list = inmuebles_list.filter(id_region=region_id)

    # Verifica si el usuario es arrendador
    if request.user.is_authenticated:
        if user.tipo_usuario == 'ARRENDADOR':  # Asumiendo que 'tipo_usuario' define roles
            # Si es arrendador, solo muestra los inmuebles que él ha registrado
            inmuebles_list = inmuebles_list.filter(arrendador=user)

    # Paginación
    paginator = Paginator(inmuebles_list, 5)
    page_number = request.GET.get('page')
    inmuebles = paginator.get_page(page_number)

    context = {
        'inmuebles': inmuebles,
        'regiones': regiones,
        'comunas': comunas,
        'comuna_id': comuna_id,
        'region_id': region_id
    }

    return render(request, 'lista_inmuebles.html', context)


def detalle_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)  # Busca el inmueble por id
    return render(request, 'detalle_inmueble.html', {'inmueble': inmueble})

def actualizar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    
    # Verifica si el usuario es el arrendador del inmueble
    if request.user != inmueble.arrendador:
        raise PermissionDenied

    if request.method == 'POST':
        print(request.POST)  # Para ver los datos que se envían en la consola
        form = InmuebleForm(request.POST, request.FILES, instance=inmueble)
        if form.is_valid():
            print("El formulario es válido")  # Depura si el formulario es válido
            form.save()
            return redirect('lista_inmuebles')
        else:
            print(form.errors)  # Muestra los errores del formulario
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

def obtener_comunas(request):
    region_id = request.GET.get('region_id')
    print(f"Region ID: {region_id}")  # Para verificar el ID recibido
    comunas = Comuna.objects.filter(id_region=region_id).values('id', 'nombre_comuna')
    print(f"Comunas: {list(comunas)}")  # Para verificar las comunas que se retornan
    return JsonResponse(list(comunas), safe=False)