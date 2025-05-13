def validar_entrada(titulo, autor):
    if not titulo or not autor:
        return False, "Todos los campos son obligatorios."
    return True, ""
