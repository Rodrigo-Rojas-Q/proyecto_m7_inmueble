import os
import django

# Configura el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto_m7.settings")
django.setup()

from django.db import connection

def obtener_inmuebles_por_region():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT r.nombre_region, i.nombre, i.descripcion
            FROM inmueble_app_inmueble i
            JOIN inmueble_app_region r ON i.id_region_id = r.id
            ORDER BY r.nombre_region, i.nombre
        """)
        return cursor.fetchall()

def guardar_resultados(resultados):
    with open('inmuebles_por_region.txt', 'w', encoding='utf-8') as f:
        region_actual = ''
        for row in resultados:
            if row[0] != region_actual:
                region_actual = row[0]
                f.write(f"\n\n--- {region_actual} ---\n\n")
            f.write(f"Nombre: {row[1]}\n")
            f.write(f"Descripción: {row[2]}\n\n")

if __name__ == "__main__":
    resultados = obtener_inmuebles_por_region()
    guardar_resultados(resultados)
    print("Resultados guardados en 'inmuebles_por_region.txt'")