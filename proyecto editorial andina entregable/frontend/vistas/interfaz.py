# frontend/vistas/interfaz.py

import tkinter as tk
from .tabla_autores import TablaAutores
from .tabla_libros import TablaLibros

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Editorial Andina - Gestión")
        self.ventana.geometry("400x300")

        tk.Label(self.ventana, text="Menú Principal", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.ventana, text="Gestión de Autores", width=25, command=self.mostrar_autores).pack(pady=5)
        tk.Button(self.ventana, text="Gestión de Libros", width=25, command=self.mostrar_libros).pack(pady=5)

    def mostrar_autores(self):
        autores = TablaAutores(self.ventana)
        autores.mostrar_tabla()

    def mostrar_libros(self):
        libros = TablaLibros(self.ventana)
        libros.mostrar_tabla()

    def mostrar_interfaz(self):
        self.ventana.mainloop()
