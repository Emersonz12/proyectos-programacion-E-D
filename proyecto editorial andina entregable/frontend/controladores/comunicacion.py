# controladores/comunicaciones.py
import requests

API_BASE = "http://127.0.0.1:8000/api"

# Funciones para AUTOR
def obtener_autores():
    try:
        response = requests.get(f"{API_BASE}/autores/")
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error al obtener autores: {e}")
    return []

def registrar_autor(nombre, nacionalidad, edad):
    try:
        data = {"nombre": nombre, "nacionalidad": nacionalidad, "edad": edad}
        response = requests.post(f"{API_BASE}/autores/", json=data)
        return response.status_code == 201
    except Exception as e:
        print(f"Error al registrar autor: {e}")
    return False

def eliminar_autor_por_id(autor_id):
    try:
        response = requests.delete(f"{API_BASE}/autores/{autor_id}/")
        return response.status_code == 204
    except Exception as e:
        print(f"Error al eliminar autor: {e}")
    return False

# Funciones para LIBRO
def obtener_libros():
    try:
        response = requests.get(f"{API_BASE}/libros/")
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error al obtener libros: {e}")
    return []

def registrar_libro(titulo, genero, paginas, anio):
    try:
        data = {"titulo": titulo, "genero": genero, "paginas": paginas, "anio": anio}
        response = requests.post(f"{API_BASE}/libros/", json=data)
        return response.status_code == 201
    except Exception as e:
        print(f"Error al registrar libro: {e}")
    return False

def eliminar_libro_por_id(libro_id):
    try:
        response = requests.delete(f"{API_BASE}/libros/{libro_id}/")
        return response.status_code == 204
    except Exception as e:
        print(f"Error al eliminar libro: {e}")
    return False
