import tkinter as tk
from tkinter import ttk
from controladores.comunicacion import obtener_literatura

class Tabla:
    def __init__(self, master):
        self.master = master
        self.tree = ttk.Treeview(master, columns=("id", "titulo", "autor"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("titulo", text="Título")
        self.tree.heading("autor", text="Autor")

    def mostrar_tabla(self):
        self.tree.pack(fill=tk.BOTH, expand=True)
        datos = obtener_literatura()
        for item in datos:
            self.tree.insert("", "end", values=(item['id'], item['titulo'], item['autor']))
