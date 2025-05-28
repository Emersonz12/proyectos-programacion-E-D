# frontend/vistas/tabla_autores.py

import tkinter as tk
from tkinter import ttk, messagebox
from controladores.comunicacion import obtener_autores, registrar_autor, eliminar_autor
from controladores.validaciones import validar_autor

class TablaAutores:
    def __init__(self, root):
        self.root = root

    def mostrar_tabla(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Gestión de Autores")
        ventana.geometry("500x400")

        tk.Label(ventana, text="Nombre").grid(row=0, column=0)
        nombre = tk.Entry(ventana)
        nombre.grid(row=0, column=1)

        tk.Label(ventana, text="Nacionalidad").grid(row=1, column=0)
        nacionalidad = tk.Entry(ventana)
        nacionalidad.grid(row=1, column=1)

        tk.Label(ventana, text="Edad").grid(row=2, column=0)
        edad = tk.Entry(ventana)
        edad.grid(row=2, column=1)

        tk.Label(ventana, text="ID a eliminar").grid(row=3, column=0)
        id_eliminar = tk.Entry(ventana)
        id_eliminar.grid(row=3, column=1)

        def registrar():
            valido, mensaje = validar_autor(nombre.get(), nacionalidad.get(), edad.get())
            if not valido:
                messagebox.showwarning("Validación", mensaje)
                return
            data = {
                "nombre": nombre.get(),
                "nacionalidad": nacionalidad.get(),
                "edad": edad.get()
            }
            if registrar_autor(data):
                messagebox.showinfo("Éxito", "Autor registrado correctamente.")

        def eliminar():
            if eliminar_autor(id_eliminar.get()):
                messagebox.showinfo("Eliminado", "Autor eliminado correctamente.")

        def ver():
            lista_win = tk.Toplevel(ventana)
            lista_win.title("Lista de Autores")
            tree = ttk.Treeview(lista_win, columns=("ID", "Nombre", "Nacionalidad", "Edad"), show="headings")
            for col in tree["columns"]:
                tree.heading(col, text=col)
            tree.pack(fill=tk.BOTH, expand=True)
            for autor in obtener_autores():
                tree.insert("", "end", values=(autor["id"], autor["nombre"], autor["nacionalidad"], autor["edad"]))

        tk.Button(ventana, text="Registrar", command=registrar).grid(row=4, column=0, columnspan=2, pady=5)
        tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=5, column=0, columnspan=2, pady=5)
        tk.Button(ventana, text="Ver Todos", command=ver).grid(row=6, column=0, columnspan=2, pady=5)
