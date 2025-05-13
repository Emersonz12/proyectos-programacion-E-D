import requests

def obtener_literatura():
    try:
        respuesta = requests.get("http://127.0.0.1:8000/api/literatura/")
        if respuesta.status_code == 200:
            return respuesta.json()
    except Exception as e:
        print(f"Error al obtener datos: {e}")
    return []
