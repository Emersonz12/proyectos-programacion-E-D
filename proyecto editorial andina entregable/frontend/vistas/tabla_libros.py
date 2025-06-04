# frontend/vistas/tabla_libros.py

import tkinter as tk
from tkinter import ttk, messagebox
from controladores.comunicacion import obtener_libros, registrar_libro, eliminar_libro
from controladores.validaciones import validar_libro

class TablaLibros:
    def __init__(self, root):
        self.root = root

    def mostrar_tabla(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Gestión de Libros")
        ventana.geometry("550x450")

        tk.Label(ventana, text="Título").grid(row=0, column=0)
        titulo = tk.Entry(ventana)
        titulo.grid(row=0, column=1)

        tk.Label(ventana, text="Género").grid(row=1, column=0)
        genero = tk.Entry(ventana)
        genero.grid(row=1, column=1)

        tk.Label(ventana, text="Páginas").grid(row=2, column=0)
        paginas = tk.Entry(ventana)
        paginas.grid(row=2, column=1)

        tk.Label(ventana, text="Año").grid(row=3, column=0)
        anio = tk.Entry(ventana)
        anio.grid(row=3, column=1)

        tk.Label(ventana, text="ID a eliminar").grid(row=4, column=0)
        id_eliminar = tk.Entry(ventana)
        id_eliminar.grid(row=4, column=1)

        def registrar():
            valido, mensaje = validar_libro(titulo.get(), genero.get(), paginas.get(), anio.get())
            if not valido:
                messagebox.showwarning("Validación", mensaje)
                return
            data = {
                "titulo": titulo.get(),
                "genero": genero.get(),
                "paginas": paginas.get(),
                "anio": anio.get()
            }
            if registrar_libro(data):
                messagebox.showinfo("Éxito", "Libro registrado correctamente.")

        def eliminar():
            if eliminar_libro(id_eliminar.get()):
                messagebox.showinfo("Eliminado", "Libro eliminado correctamente.")

        def ver():
            lista_win = tk.Toplevel(ventana)
            lista_win.title("Lista de Libros")
            tree = ttk.Treeview(lista_win, columns=("ID", "Título", "Género", "Páginas", "Año"), show="headings")
            for col in tree["columns"]:
                tree.heading(col, text=col)
            tree.pack(fill=tk.BOTH, expand=True)
            for libro in obtener_libros():
                tree.insert("", "end", values=(libro["id"], libro["titulo"], libro["genero"], libro["paginas"], libro["anio"]))

        tk.Button(ventana, text="Registrar", command=registrar).grid(row=5, column=0, columnspan=2, pady=5)
        tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=6, column=0, columnspan=2, pady=5)
        tk.Button(ventana, text="Ver Todos", command=ver).grid(row=7, column=0, columnspan=2, pady=5)
