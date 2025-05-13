import tkinter as tk
from .tabla import Tabla

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Literatura Manga")
        self.tabla = Tabla(self.ventana)

    def mostrar_interfaz(self):
        self.tabla.mostrar_tabla()
        self.ventana.mainloop()
