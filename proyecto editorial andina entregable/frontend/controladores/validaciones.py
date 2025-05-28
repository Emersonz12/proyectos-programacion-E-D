# controladores/validaciones.py

def validar_autor(nombre, nacionalidad, edad):
    if not nombre or not nacionalidad or not edad:
        return False, "Todos los campos del autor son obligatorios."
    if not edad.isdigit() or int(edad) <= 0:
        return False, "La edad debe ser un número válido mayor que cero."
    return True, ""

def validar_libro(titulo, genero, paginas, anio):
    if not titulo or not genero or not paginas or not anio:
        return False, "Todos los campos del libro son obligatorios."
    if not paginas.isdigit() or int(paginas) <= 0:
        return False, "Las páginas deben ser un número válido mayor que cero."
    if not anio.isdigit() or int(anio) <= 0:
        return False, "El año debe ser un número válido mayor que cero."
    return True, ""
