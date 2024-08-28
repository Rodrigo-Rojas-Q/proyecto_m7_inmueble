from inmueble_app.models import Inmueble, User

def get_all_inmuebles():
    inmuebles = Inmueble.objects.all()
    return inmuebles

def insertar_inmueble(data):
    try:
        # Intentar obtener la instancia del usuario
        user_instance = User.objects.get(pk=data['id_user'])
    except User.DoesNotExist:
        # Manejar el caso donde el usuario no existe
        print(f"El usuario con id {data['id_user']} no existe.")
        return None
    
    # Si el usuario existe, crear el inmueble
    inm = Inmueble(
        nombre = data['nombre'],
        descripcion=data['descripcion'],
        m2_construidos=data['m2_construidos'],
        m2_terreno=data['m2_terreno'],
        numero_estacionamientos=data['numero_estacionamientos'],
        numero_habitaciones=['numero_habitaciones'],
        numero_banos=data['numero_banos'],
        direccion=data['direccion'],
        id_user=data['id_user'],
        id_comuna=data['id_comuna'],
        id_region=data['id_region'],
        tipo_inmueble=data['tipo_inmueble'],   
        precio_mensual=data['precio_mensual'],
        estado=data['estado']
    )
    inm.save()

def actualizar_descrp_inmueble(id_inmueble, new_descrip):
    try:
        inmueble = Inmueble.objects.get(pk=id_inmueble)
        inmueble.descripcion = new_descrip
        inmueble.save()
    except Inmueble.DoesNotExist:
        return None
    
def eliminar_inmueble(id_inmueble):
    try:
        inmueble = Inmueble.objects.get(id=id_inmueble)
        inmueble.delete()
    except Inmueble.DoesNotExist:
        return None
    

